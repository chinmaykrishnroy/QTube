import os

from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QUrl, QSize, QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QFileDialog
from videowindow import VideoWindow


class MediaPlayer(QThread):
    positionChanged = pyqtSignal(int)
    durationChanged = pyqtSignal(int)
    volumeChanged = pyqtSignal(int)
    stateChanged = pyqtSignal(QMediaPlayer.State)
    mediaChanged = pyqtSignal(str)

    def __init__(self, ui, mainwindow):
        super().__init__()
        self.ui = ui
        self.mainwindow = mainwindow

        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.playlist = QMediaPlaylist()
        self.media_player.setPlaylist(self.playlist)
        self.media_player.setVolume(self.mainwindow.current_volume)
        self.ui.mediaVolumeSlider.setValue(self.mainwindow.current_volume)
        self.media_player.setPlaybackRate(self.mainwindow.playback_speed)

        self.resetLabel = QTimer(self)
        self.resetLabel.setSingleShot(True)
        self.resetLabel.timeout.connect(self.reset_media_title)

        self.is_video = False
        self.is_docked = True
        self.duration = 0
        self.current_filename = ""

        self.video_window = None

        self.connect_ui()
        self.load_media_files()
        self.connect_signals()
        self.ui.videoOutputFrame.hide()
        self.ui.videoOutputFrame.setMinimumSize(
            QSize(int(self.mainwindow.video_aspect_ratio * self.mainwindow.minimum_video_height),
                  self.mainwindow.minimum_video_height))
        self.media_player.setVideoOutput(self.ui.videoOutputFrame)
        self.ui.videoOutputFrame.mouseDoubleClickEvent = self.toggle_fullscreen
        self.ui.mediaTitleLabel.setText(f"Player Initialized!")
        self.ui.mediaTitleLabel.setToolTip(f"PyPlayer: Player Standby Mode")
        QTimer.singleShot(self.mainwindow.label_timeout,
                          lambda: self.ui.mediaTitleLabel.setText(f"PyPlayer: Player Standby Mode"))

    def connect_ui(self):
        self.ui.playbackProgress.sliderMoved.connect(self.set_position)
        self.ui.mediaVolumeSlider.sliderMoved.connect(self.set_volume)
        self.ui.mediaPlayBtn.clicked.connect(self.play_pause)
        self.ui.mediaNextBtn.clicked.connect(self.next)
        self.ui.mediaPreviousBtn.clicked.connect(self.previous)
        self.ui.seekForwardBtn.clicked.connect(lambda: self.seek(10000))
        self.ui.seekBackwardBtn.clicked.connect(lambda: self.seek(-10000))
        self.ui.playerOffBtn.clicked.connect(self.stop)
        self.ui.mediaMuteBtn.clicked.connect(self.mute_unmute)
        self.ui.playSoundBtn.clicked.connect(self.mute_unmute)
        self.ui.mediaRepeatBtn.clicked.connect(self.toggle_repeat)
        self.ui.mediaShuffleBtn.clicked.connect(self.toggle_shuffle)
        self.ui.playbackSpeedCombobox.currentIndexChanged.connect(
            self.set_playback_speed)
        self.ui.videoWidgetBtn.clicked.connect(self.toggle_fullscreen)
        self.ui.fileOpenBtn.clicked.connect(self.select_new_folder)
        self.ui.mediaLockBtn.clicked.connect(self.lock_player)

    def connect_signals(self):
        self.media_player.positionChanged.connect(self.update_position)
        self.media_player.durationChanged.connect(self.update_duration)
        self.media_player.volumeChanged.connect(self.update_volume)
        self.media_player.stateChanged.connect(self.update_state)
        self.playlist.currentMediaChanged.connect(self.update_media)

    def run(self):
        self.exec_()

    @pyqtSlot(int)
    def set_position(self, position):
        self.media_player.setPosition(position)

    @pyqtSlot(int)
    def set_volume(self, volume):
        self.media_player.setVolume(volume)
        self.mainwindow.current_volume = volume

    @pyqtSlot()
    def play_pause(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()
            if self.is_video and self.is_docked:
                self.ui.videoOutputFrame.show()

    @pyqtSlot()
    def stop(self):
        self.ui.videoOutputFrame.hide()
        self.media_player.stop()
        self.ui.mediaTitleLabel.setText(f"PyPlayer: Stopped!")
        self.ui.mediaTitleLabel.setToolTip(f"PyPlayer: Stopped!")
        self.resetLabel.start(self.mainwindow.label_timeout)
        self.ui.mediaPlayBtn.setIcon(QIcon(":/icons/icons/cil-media-play.png"))
        self.media_player.setVolume(int(self.mainwindow.default_volume))
        if self.video_window:
            self.media_player.setVideoOutput(self.ui.videoOutputFrame)
            self.video_window.close()
            self.video_window = None
            self.is_docked = True

    @pyqtSlot()
    def next(self):
        self.playlist.next()
        if not self.is_docked:
            print("In here in next")
            self.ui.videoOutputFrame.hide()

    @pyqtSlot()
    def previous(self):
        self.playlist.previous()
        if not self.is_docked:
            print("In here in next")
            self.ui.videoOutputFrame.hide()

    @pyqtSlot()
    def seek(self, milliseconds):
        self.media_player.setPosition(
            self.media_player.position() + milliseconds)

    @pyqtSlot()
    def change_volume(self, amount):
        self.mainwindow.current_volume += amount
        self.mainwindow.current_volume = max(
            0, min(self.mainwindow.current_volume, 100))
        self.media_player.setVolume(self.mainwindow.current_volume)

    @pyqtSlot()
    def mute_unmute(self):
        self.mainwindow.is_muted = not self.mainwindow.is_muted
        self.media_player.setMuted(self.mainwindow.is_muted)
        self.ui.playSoundBtn.setIcon(
            QIcon(":/icons/icons/volume-x.svg" if self.mainwindow.is_muted else ":/icons/icons/volume-2.svg"))
        self.ui.playSoundBtn.setText(
            "Disabled" if self.mainwindow.is_muted else "Enabled")
        self.mainwindow.pushNotification(
            ("Media Volume Disabled" if self.mainwindow.is_muted else "Media Volume Enabled"), 0)
        self.ui.mediaMuteBtn.setIcon(QIcon(
            ":/icons/icons/cil-volume-off.png" if self.mainwindow.is_muted else ":/icons/icons/cil-volume-high.png"))
        self.ui.mediaVolumeSlider.setEnabled(not self.mainwindow.is_muted)

    @pyqtSlot()
    def toggle_repeat(self):
        self.mainwindow.repeat_mode = (self.mainwindow.repeat_mode + 1) % 3
        playback_modes = [QMediaPlaylist.Sequential,
                          QMediaPlaylist.Loop, QMediaPlaylist.CurrentItemInLoop]
        icons = ["cil-loop.png", "cil-loop-circular.png", "cil-loop-1.png"]
        self.playlist.setPlaybackMode(
            playback_modes[self.mainwindow.repeat_mode])
        self.ui.mediaRepeatBtn.setIcon(
            QIcon(f":/icons/icons/{icons[self.mainwindow.repeat_mode]}"))

    @pyqtSlot()
    def toggle_shuffle(self):
        self.mainwindow.is_shuffled = not self.mainwindow.is_shuffled
        self.playlist.setPlaybackMode(
            QMediaPlaylist.Random if self.mainwindow.is_shuffled else QMediaPlaylist.Sequential)
        self.ui.mediaShuffleBtn.setIcon(
            QIcon(":/icons/icons/cil-layers.png" if self.mainwindow.is_shuffled else ":/icons/icons/cil-infinity.png"))

    @pyqtSlot(int)
    def set_playback_speed(self):
        speed = float(
            self.ui.playbackSpeedCombobox.currentText().replace('x', ''))
        self.media_player.setPlaybackRate(speed)

    @pyqtSlot()
    def toggle_fullscreen(self, event=None):
        if self.is_video:
            if self.video_window:
                self.ui.videoOutputFrame.show()
                self.media_player.setVideoOutput(self.ui.videoOutputFrame)
                self.video_window.close()
                self.video_window = None
                self.is_docked = True
            else:
                self.video_window = VideoWindow(self.ui, self)
                self.media_player.setVideoOutput(
                    self.video_window.video_widget)
                self.video_window.show()
                self.ui.videoOutputFrame.hide()
                self.is_docked = False
                self.mainwindow.pushNotification(
                    "Double Click on Video Window to Toggle Full Screen", 0)
        else:
            self.mainwindow.pushNotification(
                "Can't Undock Player for Audio", 0)

    @pyqtSlot()
    def select_new_folder(self, folder=None):
        if folder is None:
            folder = QFileDialog.getExistingDirectory(
                self.ui.centralwidget, "Select Media Folder")
        if folder:
            media_files = []
            existing_files = set(self.mainwindow.media_files)

            # Check against existing playlist files
            for i in range(self.playlist.mediaCount()):
                existing_files.add(self.playlist.media(
                    i).canonicalUrl().toLocalFile())

            for root, _, files in os.walk(folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    if any(file.lower().endswith(ext) for ext in
                           self.mainwindow.audio_formats + self.mainwindow.video_formats):
                        if file_path not in existing_files:
                            media_files.append(file_path)
                            existing_files.add(file_path)

            if media_files:
                self.mainwindow.media_files.extend(media_files)
                self.add_files_to_playlist(media_files)
                self.ui.mediaTitleLabel.setText(f"Added Media Files")
                self.resetLabel.start(self.mainwindow.label_timeout)

    def lock_player(self):
        self.mainwindow.is_locked = not self.mainwindow.is_locked
        lock_buttons = [
            self.ui.mediaNextBtn, self.ui.mediaPreviousBtn, self.ui.seekForwardBtn,
            self.ui.seekBackwardBtn, self.ui.mediaMuteBtn, self.ui.mediaRepeatBtn,
            self.ui.mediaShuffleBtn, self.ui.playbackSpeedCombobox, self.ui.videoWidgetBtn,
            self.ui.fileOpenBtn, self.ui.mediaPlayBtn, self.ui.mediaVolumeSlider,
            self.ui.playbackProgress
        ]
        for button in lock_buttons:
            button.setEnabled(not self.mainwindow.is_locked)
        self.ui.mediaLockBtn.setIcon(
            QIcon(f":/icons/icons/cil-lock-{'unlocked' if self.mainwindow.is_locked else 'locked'}.png"))

    def load_media_files(self):
        if self.mainwindow.media_files:
            self.add_files_to_playlist(self.mainwindow.media_files)

    def add_files_to_playlist(self, files):
        for file in files:
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(file)))

    def update_position(self, position):
        self.ui.playbackProgress.setValue(position)
        self.ui.currentPlayingTimeLabel.setText(self.format_time(position))
        self.ui.mediaLengthLabel.setText(
            f"{self.format_time(self.duration - position)}")

    def update_duration(self, duration):
        self.duration = duration
        self.ui.playbackProgress.setMaximum(duration)

    def update_volume(self, volume):
        self.ui.mediaVolumeSlider.setValue(volume)

    def update_state(self, state):
        icons = {QMediaPlayer.PlayingState: "cil-media-pause.png",
                 QMediaPlayer.PausedState: "cil-media-play.png"}
        self.ui.mediaPlayBtn.setIcon(
            QIcon(f":/icons/icons/{icons.get(state, 'cil-media-play.png')}"))

    def update_media(self, media):
        if media.isNull():
            self.stop()
            self.ui.mediaTitleLabel.setText(f"End of Playlist!")
            self.ui.mediaTitleLabel.setToolTip(f"End of Playlist!")
            self.resetLabel.start(int(self.mainwindow.label_timeout))
            self.mainwindow.pushNotification(
                f"No More Files to Play, Try Adding Directory Containing Media Files From Folder Button.")
            QTimer.singleShot(self.mainwindow.label_timeout + self.mainwindow.notification_popup_timeout,
                              lambda: self.mainwindow.pushNotification(
                                  f"You Can Use Repeat Button to Loop the Playlist."))
            return
        file_path = media.canonicalUrl().toLocalFile()
        self.is_video = any(
            format in file_path for format in self.mainwindow.video_formats)
        self.ui.videoOutputFrame.show(
        ) if self.is_video and self.is_docked else self.ui.videoOutputFrame.hide()
        if not self.is_docked and not self.is_video:
            self.video_window.close()
            self.video_window = None
            self.is_docked = True
            self.media_player.setVideoOutput(self.ui.videoOutputFrame)
        self.current_filename = media.canonicalUrl().fileName()
        self.ui.mediaTitleLabel.setText(media.canonicalUrl().fileName())
        self.ui.mediaTitleLabel.setToolTip(media.canonicalUrl().fileName())
        self.ui.playerTitleLabel.setText(media.canonicalUrl().fileName())

    def format_time(self, ms):
        seconds = (ms / 1000) % 60
        minutes = (ms / (1000 * 60)) % 60
        hours = (ms / (1000 * 60 * 60)) % 24
        if int(hours) > 0:
            return "%02d:%02d:%02d" % (hours, minutes, seconds)
        else:
            return "%02d:%02d" % (minutes, seconds)

    def play_media_from_path(self, file_path):
        try:
            self.is_video = any(
                format in file_path for format in self.mainwindow.video_formats)
            self.ui.videoOutputFrame.show(
            ) if self.is_video and self.is_docked else self.ui.videoOutputFrame.hide()
            if not self.is_docked and not self.is_video:
                self.video_window.close()
                self.video_window = None
                self.is_docked = True
                self.media_player.setVideoOutput(self.ui.videoOutputFrame)
            media_url = QUrl.fromLocalFile(file_path)
            for i in range(self.playlist.mediaCount() - 1, -1, -1):
                if self.playlist.media(i).canonicalUrl() == media_url:
                    self.playlist.removeMedia(i)
            self.playlist.insertMedia(0, QMediaContent(media_url))
            self.playlist.setCurrentIndex(0)
            self.media_player.play()
        except Exception as e:
            self.mainwindow.pushNotification(
                f"Can't Play Media Due to Exception: {e}")

    def reset_media_title(self):
        if self.current_filename:
            self.ui.mediaTitleLabel.setText(self.current_filename)
            self.ui.mediaTitleLabel.setToolTip(self.current_filename)
        else:
            self.ui.mediaTitleLabel.setText(f"PyPlayer: Player Standby Mode")
            self.ui.mediaTitleLabel.setToolTip(
                f"PyPlayer: Player Standby Mode")

    def cleanup_before_exit(self):
        if self.video_window is not None:
            self.video_window.close()
            self.video_window = None
        self.media_player.stop()
        self.quit()
        self.wait()
