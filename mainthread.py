import json
import os
import random
import re
import sys
import webbrowser
import res_rc

from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QUrl
from PyQt5.QtGui import QMovie, QDragEnterEvent, QDropEvent
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

from filethread import FileWatcherSystem
from historymanager import HistoryManager
from interface import *
from internetcheckerthread import InternetChecker, SignalEmitter
from mediaplayerthread import MediaPlayer
from searchthread import SearchThread


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.left_menu_container_min_width = 48
        self.left_menu_container_max_width = 150
        self.setting_help_width = 200
        self.ui.centerMenuSubContainer.hide()
        self.ui.notificationFrame.hide()
        self.loadState()
        self.setWindowIcon(QIcon(":/icons/icons/youtube.svg"))
        self.setAcceptDrops(True)
        self.show()

        self.soundPlayer = QMediaPlayer()
        # self.sound_enabled = True
        self.playSound('%s/sound/drop.wav' % os.getcwd(), 50)

        # self.current_stack = 0
        self.setting_menu_visible = False
        self.help_menu_visible = False
        # self.allow_notification_popups = True
        self.default_files = []
        self.notification_popup_timeout = 5000
        # self.default_download_directory = "%s\\Downloads"%os.getcwd()
        self.app_directory = os.getcwd()
        self.ui.videoExtensionComboBox.setCurrentIndex(
            self.default_video_extension_index)
        self.default_video_extension = self.ui.videoExtensionComboBox.currentText()
        self.ui.audioExtensionComboBox.setCurrentIndex(
            self.default_audio_extension_index)
        self.default_audio_extension = self.ui.audioExtensionComboBox.currentText()
        self.ui.defaultVolumeComboBox.setCurrentIndex(
            self.default_volume_index)
        self.default_volume = int(self.ui.defaultVolumeComboBox.currentText())
        self.ui.playbackSpeedCombobox.setCurrentIndex(2)
        self.playback_speed = float(
            self.ui.playbackSpeedCombobox.currentText().replace('x', ''))
        self.ui.filesSortComboBox.setCurrentIndex(self.default_sort_index)
        self.file_sorting_key = str(self.ui.filesSortComboBox.currentText())
        self.video_formats = [".webm", ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", "mpeg", ".3gp", ".mts", ".ts",
                              ".vob"]
        self.audio_formats = [".mp3", ".wav",
                              ".aac", ".m4a", ".flac", ".ogg", ".wma"]
        self.animation_time = 150
        self.label_timeout = 2500
        # self.dark_theme = True
        # self.allow_random_initial_query = False

        self.network_speed = "0B/s"
        self.has_internet = True
        self.internet_connected = True

        self.edge_margin = 8
        self.resizing = False
        self.dragging = False
        self.resize_position = None
        self.drag_position = None
        self.video_aspect_ratio = 16 / 9
        self.minimum_video_height = 480

        self.media_files = []
        self.is_muted = False
        self.repeat_mode = 0
        self.is_shuffled = False
        self.is_locked = False
        self.loggerText = ""

        self.default_search_prompts = [
            "Trending Now", "Top Music Videos", "Latest World News", "Top English Music Videos",
            "Popular Gaming Videos", "Top Movies Trailers",
            "Trending English Comedy Clips", "Best of Sports Highlights",
            "Popular Documentary", "Latest Tech Reviews English", "Top World Wide Vlog",
            "Popular Physics Documentary", "Cosmos", "Space and Research", "Top Scientific Videos",
            "Popular Computer Documentary"
        ]

        self.file_watcher_system = FileWatcherSystem(
            self.default_download_directory, self)
        self.file_watcher_system.files_changed.connect(self.updateFiles)

        self.history_manager = HistoryManager(self.app_directory)
        self.history_list = self.history_manager.get_history()

        self.signal_emitter = SignalEmitter()
        self.signal_emitter.connection_status_changed.connect(
            self.updateInternetStatus)

        self.internet_checker = InternetChecker(self.signal_emitter)
        self.internet_checker.start()

        QTimer.singleShot(500, self.initMediaPlayer)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.checkInternetStatus)
        self.timer.start(3000)

        self.dots = ""
        self.dots_timer = QTimer(self)
        self.dots_timer.timeout.connect(self.updateDots)
        self.dots_timer.start(500)

        self.reset_placeholder = QTimer(self)
        self.reset_placeholder.setSingleShot(True)
        self.reset_placeholder.timeout.connect(self.resetPlacehlder)

        self.sideBarAnimation = QPropertyAnimation(
            self.ui.leftMenuContainer, b"minimumWidth")
        self.sideBarAnimation.setDuration(self.animation_time)
        self.sideBarAnimation.setEasingCurve(QEasingCurve.InOutExpo)

        self.settingHelpAnimation = QPropertyAnimation(
            self.ui.centerMenuContainer, b"minimumWidth")
        self.settingHelpAnimation.setDuration(int(0.5 * self.animation_time))
        self.settingHelpAnimation.setEasingCurve(QEasingCurve.Linear)

        self.notificationAnimation = QPropertyAnimation(
            self.ui.notificationWiget, b"minimumHeight")
        self.notificationAnimation.setDuration(int(1.75 * self.animation_time))
        self.notificationAnimation.setEasingCurve(QEasingCurve.InOutBack)

        self.ui.appCloseBtn.clicked.connect(lambda: self.close())
        self.ui.appMinBtn.clicked.connect(self.setMinimized)
        self.ui.appMaxBtn.clicked.connect(self.toggleMaximized)
        self.ui.menuToggleBtn.clicked.connect(self.toggleSidebar)
        self.ui.homeMenuBtn.clicked.connect(self.showSearchStack)
        self.ui.downloadMenuBtn.clicked.connect(self.showDownloadStack)
        self.ui.fileMenuBtn.clicked.connect(self.showFileStack)
        self.ui.historyMenuBtn.clicked.connect(self.showHistoryStack)
        self.ui.closeSettingMenuBtn.clicked.connect(self.hidesettingHelpMenu)
        self.ui.closeHelpMenuBtn.clicked.connect(self.hidesettingHelpMenu)
        self.ui.settingsBtn.clicked.connect(self.showSettingMenu)
        self.ui.helpBtn.clicked.connect(self.showHelpMenu)
        self.ui.filesSortComboBox.currentIndexChanged.connect(
            self.updateFilesWithNewSortingMethod)
        self.ui.forceRescanBtn.clicked.connect(self.refreshFiles)
        self.ui.randInitBtn.clicked.connect(self.toggleInitialRandomSearch)
        self.ui.appSoundBtn.clicked.connect(self.handleAppSound)
        self.ui.folderSelectBtn.clicked.connect(
            self.selectDefaultDownloadDirectory)
        self.ui.videoExtensionComboBox.currentIndexChanged.connect(
            self.updateDefaultVideoExtension)
        self.ui.audioExtensionComboBox.currentIndexChanged.connect(
            self.updateDefaultAudioExtension)
        self.ui.defaultVolumeComboBox.currentIndexChanged.connect(
            self.updateDefaultVolume)
        self.ui.searchBtn.clicked.connect(self.searchVideos)
        self.ui.darkModeBtn.clicked.connect(self.toggleTheme)
        self.ui.themeBtn.clicked.connect(self.toggleTheme)
        self.ui.notificationBtn.clicked.connect(self.enableNotification)
        self.ui.networkBtn.clicked.connect(self.showKitten)
        self.ui.clearNotificationBtn.clicked.connect(self.hideNotificationTab)
        self.ui.youtubeIconBtn.clicked.connect(self.redirectYouTube)
        self.ui.githubProfileBtn.clicked.connect(self.redirectGithub)
        self.ui.linkedinProfileBtn.clicked.connect(self.redirectLinkedIn)
        self.ui.instagramProfileBtn.clicked.connect(self.redirectInstagram)
        self.ui.loggerBtn.clicked.connect(self.toggleLogger)

        self.ui.addHistory(self.history_list)
        self.ui.homeRedirect()
        self.ui.endOfFile()
        if self.allow_random_initial_query:
            self.startVideoSearch(random.choice(self.default_search_prompts))
        else:
            video_info_list = []
            for _ in range(random.randint(9, 12)):
                video_element = {
                    "id": f"{_}", "title": f"Video Title Will Appear Here",
                    "duration": f"{random.randint(0, 59)}:{random.randint(1, 59)}",
                    "channel": f"Channel Name", "views": f"{random.randint(1, 1000)}B views",
                    "time": f"{random.randint(50, 90)} years ago"
                }
                video_info_list.append(video_element)
            self.ui.addVideos(video_info_list, self)
        QTimer.singleShot(
            2000, lambda: self.ui.mainAppStack.setCurrentIndex(self.current_stack))

    def updateDots(self):
        if len(self.dots) < 3:
            self.dots += "."
        else:
            self.dots = ""
        self.ui.loadingLabel.setText(f"Loading{self.dots}")
        self.ui.initLabel.setText(f"Initializing{self.dots}")

    def initMediaPlayer(self):
        self.media_files = [d['path']
                            for d in self.default_files if 'path' in d]
        self.media_player = MediaPlayer(self.ui, self)
        self.media_player.start()

    def defaultVolumeUpdate(self):
        self.defaultVolume = int(self.ui.defaultVolumeComboBox.currentText())

    def playSound(self, path, volume=15):
        if self.sound_enabled:
            try:
                self.soundPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(path)))
                self.soundPlayer.setVolume(volume)
                self.soundPlayer.play()
            except Exception as e:
                print("Can't play tones! ", e)

    def handleAppSound(self):
        self.sound_enabled = not self.sound_enabled
        if self.sound_enabled:
            self.ui.appSoundBtn.setText("Enabled")
            self.pushNotification("Notification Sounds Enabled")
        else:
            self.ui.appSoundBtn.setText("Disabled")
            self.pushNotification("Notification Sounds Disabled")

    def showSearchStack(self):
        self.playSound('%s/sound/tap2.mp3' % os.getcwd())
        if self.ui.mainAppStack.currentIndex() != 0:
            self.ui.mainAppStack.setCurrentIndex(0)
        else:
            self.toggleSidebar()

    def showDownloadStack(self):
        self.playSound('%s/sound/tap2.mp3' % os.getcwd())
        if self.ui.mainAppStack.currentIndex() != 3:
            self.ui.mainAppStack.setCurrentIndex(3)
        else:
            self.toggleSidebar()

    def showFileStack(self):
        self.playSound('%s/sound/tap2.mp3' % os.getcwd())
        if self.ui.mainAppStack.currentIndex() != 4:
            self.ui.mainAppStack.setCurrentIndex(4)
        else:
            self.toggleSidebar()

    def showHistoryStack(self):
        self.playSound('%s/sound/tap2.mp3' % os.getcwd())
        if self.ui.mainAppStack.currentIndex() != 5:
            self.ui.mainAppStack.setCurrentIndex(5)
        else:
            self.toggleSidebar()

    def updateFiles(self, files):
        self.default_files = files
        files.sort(key=lambda x: x[self.file_sorting_key.lower()])
        self.ui.addFiles(self, files)

    def updateFilesWithNewSortingMethod(self):
        self.file_sorting_key = str(self.ui.filesSortComboBox.currentText())
        self.refreshFiles()

    def refreshFiles(self):
        self.file_watcher_system.stop()
        self.file_watcher_system.deleteLater()
        self.file_watcher_system = FileWatcherSystem(
            self.default_download_directory, self)
        self.file_watcher_system.files_changed.connect(self.updateFiles)
        self.pushNotification('Files Refreshed')

    def toggleMaximized(self):
        self.playSound('%s/sound/tap2.mp3' % os.getcwd())
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def setMinimized(self):
        self.playSound('%s/sound/tap2.mp3' % os.getcwd())
        self.showMinimized()

    def updateInternetStatus(self, status):
        icon_path = ':/icons/icons/cil-wifi-signal-4.png' if status else ':/icons/icons/cil-wifi-signal-off.png'
        self.ui.networkBtn.setIcon(QIcon(icon_path))

        if hasattr(self, 'notification_shown'):
            if self.has_internet != status:
                message = "Connected to Internet!" if status else "No Internet!"
                self.pushNotification(message)
        else:
            setattr(self, 'notification_shown', True)

        self.has_internet = status

    def checkInternetStatus(self):
        self.internet_connected = self.internet_checker.connected_to_internet
        if self.ui.currentInfoLabel.text() == self.loggerText:
            self.ui.currentInfoLabel.setText("")
        self.loggerText = self.ui.currentInfoLabel.text()
        self.ui.currentInfoLabel.setText("")
        # print(f"Does the device connected to the internet?: {self.internet_connected}")

    def toggleSidebar(self):
        self.left_menu_container_visible ^= True
        self.playSound('%s/sound/tap2.mp3' % os.getcwd())
        if self.left_menu_container_visible:
            self.sideBarAnimation.setStartValue(
                self.ui.leftMenuContainer.width())
            self.sideBarAnimation.setEndValue(
                self.left_menu_container_max_width)
        else:
            self.sideBarAnimation.setStartValue(
                self.ui.leftMenuContainer.width())
            self.sideBarAnimation.setEndValue(
                self.left_menu_container_min_width)
            self.ui.leftMenuContainer.setMaximumWidth(
                self.left_menu_container_min_width)
        self.sideBarAnimation.start()

    def hidesettingHelpMenu(self):
        self.playSound('%s/sound/tap2.mp3' % os.getcwd())
        self.settingHelpAnimation.setEndValue(0)
        self.settingHelpAnimation.start()
        self.ui.centerMenuSubContainer.hide()
        self.center_menu_container_visible = False
        self.help_menu_visible = False
        self.setting_menu_visible = False

    def showSettingMenu(self):
        self.playSound('%s/sound/tap2.mp3' % os.getcwd())
        if self.help_menu_visible and not self.setting_menu_visible:
            self.ui.centerMenuSubContainer.show()
            self.ui.settingHelpMenu.setCurrentIndex(0)
            self.center_menu_container_visible = True
            self.setting_menu_visible = True
            self.help_menu_visible = False
        elif self.setting_menu_visible:
            self.settingHelpAnimation.setStartValue(
                self.ui.centerMenuContainer.width())
            self.settingHelpAnimation.setEndValue(0)
            self.settingHelpAnimation.start()
            self.ui.centerMenuSubContainer.hide()
            self.center_menu_container_visible = False
            self.setting_menu_visible = False
        elif not self.setting_menu_visible:
            self.settingHelpAnimation.setStartValue(0)
            self.settingHelpAnimation.setEndValue(self.setting_help_width)
            self.settingHelpAnimation.start()
            self.ui.centerMenuSubContainer.show()
            self.ui.settingHelpMenu.setCurrentIndex(0)
            self.center_menu_container_visible = True
            self.setting_menu_visible = True
            self.help_menu_visible = False

    def showHelpMenu(self):
        self.playSound('%s/sound/tap2.mp3' % os.getcwd())
        if self.setting_menu_visible and not self.help_menu_visible:
            self.ui.centerMenuSubContainer.show()
            self.ui.settingHelpMenu.setCurrentIndex(1)
            self.center_menu_container_visible = True
            self.help_menu_visible = True
            self.setting_menu_visible = False
        elif self.help_menu_visible:
            self.settingHelpAnimation.setStartValue(
                self.ui.centerMenuContainer.width())
            self.settingHelpAnimation.setEndValue(0)
            self.settingHelpAnimation.start()
            self.ui.centerMenuSubContainer.hide()
            self.center_menu_container_visible = False
            self.help_menu_visible = False
        elif not self.help_menu_visible:
            self.settingHelpAnimation.setStartValue(0)
            self.settingHelpAnimation.setEndValue(self.setting_help_width)
            self.settingHelpAnimation.start()
            self.ui.centerMenuSubContainer.show()
            self.ui.settingHelpMenu.setCurrentIndex(1)
            self.center_menu_container_visible = True
            self.help_menu_visible = True
            self.setting_menu_visible = False

    def enableNotification(self):
        if self.allow_notification_popups:
            self.ui.notificationBtn.setIcon(
                QIcon(':/icons/icons/cil-volume-off.png'))
            self.pushNotification("Notification turned off!")
            self.allow_notification_popups = False
        else:
            self.allow_notification_popups = True
            self.ui.notificationBtn.setIcon(
                QIcon(':/icons/icons/cil-bell.png'))
            self.pushNotification("Notification turned on!")

    def updateDefaultVideoExtension(self, index):
        self.default_video_extension = self.ui.videoExtensionComboBox.currentText()
        self.pushNotification(
            "Changed default video extension to '%s' !" % self.default_video_extension)

    def updateDefaultAudioExtension(self, index):
        self.default_audio_extension = self.ui.audioExtensionComboBox.currentText()
        self.pushNotification(
            "Changed default audio extension to '%s' !" % self.default_audio_extension)

    def pushNotification(self, notification_message, notification_volume=25, tone=True):
        # self.ui.notificationFrame.hide()
        if self.allow_notification_popups:
            if tone:
                self.playSound('%s/sound/notification.mp3' %
                               os.getcwd(), notification_volume)
            self.notificationAnimation.setStartValue(0)
            self.notificationAnimation.setEndValue(49)
            self.notificationAnimation.start()
            self.ui.notificationLabel.setMaximumHeight(49)
            self.ui.notificationLabel.setText(notification_message)
            QTimer.singleShot(int(1.5 * self.animation_time),
                              lambda: self.ui.notificationFrame.show())
            QTimer.singleShot(
                int(self.notification_popup_timeout), self.hideNotificationTab)

    def hideNotificationTab(self):
        self.notificationAnimation.setStartValue(
            self.ui.notificationWiget.height())
        self.notificationAnimation.setEndValue(0)
        self.notificationAnimation.start()
        self.ui.notificationLabel.setText("")
        self.ui.notificationFrame.hide()

    def mousePressEvent(self, event):
        rect = self.rect()
        if (
                rect.topLeft().x() + self.edge_margin >= event.x()
                or rect.bottomRight().x() - self.edge_margin <= event.x()
                or rect.topLeft().y() + self.edge_margin >= event.y()
                or rect.bottomRight().y() - self.edge_margin <= event.y()
        ):
            self.resizing = True
            self.dragging = False
            self.resize_position = event.globalPos()
        else:
            self.resizing = False
            self.dragging = True
            self.drag_position = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if self.resizing:
            delta = event.globalPos() - self.resize_position
            new_width = max(self.width() + delta.x(), 100)
            new_height = max(self.height() + delta.y(), 100)
            self.resize(new_width, new_height)
            self.resize_position = event.globalPos()
            self.setCursor(Qt.SizeFDiagCursor)
        elif self.dragging:
            self.move(event.globalPos() - self.drag_position)
            self.setCursor(Qt.SizeAllCursor)

    def mouseReleaseEvent(self, event):
        self.resizing = False
        self.dragging = False
        self.unsetCursor()

    def loadTheme(self, theme_path):
        try:
            with open(theme_path, "r") as file:
                self.setStyleSheet(file.read())
            self.initGif = QMovie(u":/gif/catDark.gif" if theme_path ==
                                  "themes/dark.theme" else u":/gif/catLight.gif")
            self.ui.initIcon.setMovie(self.initGif)
            self.ui.loadingIcon.setMovie(self.initGif)
            self.initGif.start()
        except Exception as e:
            print("Can't load theme! '%s'" % e)
            self.pushNotification(f"Theme file not found! {e}")
            self.close()
            QMessageBox.critical(self, "Error", f"Theme file not found!\n{e}")
            sys.exit(1)

    def updateDefaultVolume(self, index):
        self.default_volume = self.ui.defaultVolumeComboBox.currentText()
        self.pushNotification(
            "Default Media Volume Changed to '%s'." % self.default_volume)

    def toggleTheme(self):
        self.dark_theme ^= True
        if self.dark_theme:
            self.ui.darkModeBtn.setText("Dark")
            self.ui.darkModeBtn.setIcon(QIcon(':/icons/icons/moon.svg'))
            self.ui.themeBtn.setIcon(QIcon(':/icons/icons/cil-lightbulb.png'))
            self.loadTheme("themes/dark.theme")
            self.initGif = QMovie(u":/gif/catDark.gif")
            self.pushNotification("Theme Changed to Dark!")
        else:
            self.ui.darkModeBtn.setText("Light")
            self.ui.darkModeBtn.setIcon(QIcon(':/icons/icons/sun.svg'))
            self.ui.themeBtn.setIcon(QIcon(':/icons/icons/cil-moon.png'))
            self.loadTheme("themes/light.theme")
            self.initGif = QMovie(u":/gif/catLight.gif")
            self.pushNotification("Theme Changed to Light!")
        self.ui.loadingIcon.setMovie(self.initGif)
        self.ui.initIcon.setMovie(self.initGif)
        self.initGif.start()

    def selectDefaultDownloadDirectory(self):
        directory = QFileDialog.getExistingDirectory(
            self, "Select Default Folder", "")
        if directory:
            self.default_download_directory = directory
            self.file_watcher_system.stop()
            self.file_watcher_system.deleteLater()
            print("Selected directory:", self.default_download_directory)
            self.ui.folderSelectBtn.setText("Directory Updated")
            QTimer.singleShot(
                self.label_timeout, lambda: self.ui.folderSelectBtn.setText("Folder Selector"))
            self.pushNotification("Directory updated to '%s'." %
                                  self.default_download_directory)
            self.file_watcher_system = FileWatcherSystem(
                self.default_download_directory, self)
            self.file_watcher_system.files_changed.connect(self.updateFiles)

    def searchVideos(self):
        if self.internet_connected:
            query = self.ui.searchInputText.text().strip()
            if query:
                self.startVideoSearch(query)
            else:
                self.pushNotification(
                    "Type Something in Search Box, Query Can't be Blank!")
                self.ui.searchInputText.setPlaceholderText(
                    "Type Something, Query Can't be Blank!")
                self.reset_placeholder.start(2000)
        else:
            self.pushNotification(
                "No Internet! Connect to Stable Internet Connection.")
            self.ui.searchInputText.setPlaceholderText(
                "No Internet! Connect to Internet!")
            self.reset_placeholder.start(2000)

    def resetPlacehlder(self):
        self.ui.searchInputText.setPlaceholderText(
            "Enter Anything To Search...")

    def startVideoSearch(self, query):
        if self.internet_connected:
            self.ui.searchBtn.setEnabled(False)
            self.ui.mainAppStack.setCurrentIndex(1)
            self.search_thread = SearchThread(query, self)
            self.search_thread.search_finished.connect(self.addVideo)
            self.search_thread.start()
        else:
            self.pushNotification(
                "No Internet! Connect to Stable Internet Connection.")

    def addVideo(self, file_info_list):
        self.ui.searchBtn.setEnabled(True)
        self.ui.addVideos(file_info_list, self)
        self.search_thread.stop()
        self.search_thread.wait()
        self.search_thread.deleteLater()
        self.ui.mainAppStack.setCurrentIndex(0)

    def handlefilePlayBtnClick(self, path):
        print("Clicked on: ", path)
        self.media_player.play_media_from_path(path)

    def handleDownloadBtnClick(self, id, title):
        print("Thumbnail Button video ID: ", id, "video Title: ", title)
        try:
            try:
                int(id)
            except:
                self.ui.addDownload(id, title, self)
            self.ui.stopImageDownloaderThreads()
            self.ui.searchInputText.clear()
        except Exception as e:
            self.ui.stopImageDownloaderThreads()
            print("Can't add to download due to exception:  ", e)
            self.pushNotification(
                f"Can't add to download due to exception: {e}")

    def handleThumbnailBtnClick(self, id, title):
        print("Thumbnail Button video ID: ", id, "video Title: ", title)
        try:
            try:
                int(id)
            except:
                self.ui.addDownload(id, title, self, True)
            self.ui.stopImageDownloaderThreads()
            self.ui.searchInputText.clear()
        except Exception as e:
            self.ui.stopImageDownloaderThreads()
            print("Can't add to download due to exception:  ", e)
            self.pushNotification(
                f"Can't add to download due to exception: {e}")

    def handleStreamBtnClick(self, id, title):
        print("Stream Button video ID: ", id, "video Title: ", title)

    def saveState(self):
        state = {
            'sound_enabled': self.sound_enabled,
            'allow_notification_popups': self.allow_notification_popups,
            'default_download_directory': self.default_download_directory,
            'dark_theme': self.dark_theme,
            'allow_random_initial_query': self.allow_random_initial_query,
            'current_stack': self.ui.mainAppStack.currentIndex(),
            'current_volume': self.current_volume,
            'default_volume_index': self.ui.defaultVolumeComboBox.currentIndex(),
            'default_audio_extension_index': self.ui.audioExtensionComboBox.currentIndex(),
            'default_video_extension_index': self.ui.videoExtensionComboBox.currentIndex(),
            'default_sort_index': self.ui.filesSortComboBox.currentIndex(),
            'left_menu_visible': self.left_menu_container_visible,
            'center_menu_visible': self.center_menu_container_visible,
            'width': self.width(),
            'height': self.height(),
            'logger_visible': self.logger_visible
        }
        with open('.state.json', 'w') as f:
            json.dump(state, f)

    def loadState(self):
        default_sound_enabled = True
        default_allow_notification_popups = True
        default_download_directory = '%s\\Downloads' % os.getcwd()
        default_dark_theme = True
        default_allow_random_initial_query = False
        default_initial_stack = 0
        current_volume = 60
        default_volume_index = 2
        default_sort_index = 0
        default_audio_extension_index = 0
        default_video_extension_index = 0
        left_menu_visible = True
        center_menu_visible = False
        width_ = 1024
        height_ = 640
        logger_visible = False
        try:
            with open('.state.json', 'r') as f:
                state = json.load(f)
                self.sound_enabled = state.get(
                    'sound_enabled', default_sound_enabled)
                self.allow_notification_popups = state.get('allow_notification_popups',
                                                           default_allow_notification_popups)
                self.default_download_directory = state.get(
                    'default_download_directory', default_download_directory)
                self.dark_theme = state.get('dark_theme', default_dark_theme)
                self.allow_random_initial_query = state.get('allow_random_initial_query',
                                                            default_allow_random_initial_query)
                self.current_stack = state.get(
                    'current_stack', default_initial_stack)
                self.current_volume = state.get(
                    'current_volume', current_volume)
                self.default_volume_index = state.get(
                    'default_volume_index', default_volume_index)
                self.default_sort_index = state.get(
                    'default_sort_index', default_sort_index)
                self.default_audio_extension_index = state.get('default_audio_extension_index',
                                                               default_audio_extension_index)
                self.default_video_extension_index = state.get('default_video_extension_index',
                                                               default_video_extension_index)
                self.left_menu_container_visible = state.get(
                    'left_menu_visible', True)
                self.center_menu_container_visible = state.get(
                    'center_menu_visible', False)
                self.width_ = state.get('width', width_)
                self.height_ = state.get('height', height_)
                self.logger_visible = state.get(
                    'logger_visible', logger_visible)
        except FileNotFoundError:
            self.left_menu_container_visible = left_menu_visible
            self.center_menu_container_visible = center_menu_visible
            self.sound_enabled = default_sound_enabled
            self.allow_notification_popups = default_allow_notification_popups
            self.default_download_directory = default_download_directory
            self.dark_theme = default_dark_theme
            self.allow_random_initial_query = default_allow_random_initial_query
            self.current_stack = default_initial_stack
            self.current_volume = current_volume
            self.default_volume_index = default_volume_index
            self.default_audio_extension_index = default_audio_extension_index
            self.default_video_extension_index = default_video_extension_index
            self.default_sort_index = default_sort_index
            self.logger_visible = logger_visible
            self.width_ = width_
            self.height_ = height_
        self.resize(self.width_, self.height_)
        if not self.left_menu_container_visible:
            self.ui.leftMenuContainer.setMaximumWidth(
                self.left_menu_container_min_width)
        if self.center_menu_container_visible:
            self.ui.centerMenuSubContainer.show()
        self.loadTheme(
            "themes/dark.theme") if self.dark_theme else self.loadTheme("themes/light.theme")
        self.ui.appSoundBtn.setText(
            "Enabled" if self.sound_enabled else "Disabled")
        self.ui.currentInfoLabel.show() if self.logger_visible else self.ui.currentInfoLabel.hide()
        self.ui.loggerBtn.setText(
            "Enabled" if self.logger_visible else "Disabled")
        self.ui.randInitBtn.setText(
            "Enabled" if self.allow_random_initial_query else "Disabled")
        self.ui.notificationBtn.setIcon(
            QIcon(':/icons/icons/cil-bell.png' if self.allow_notification_popups else ':/icons/icons/cil-volume-off.png'))
        self.ui.themeBtn.setIcon(QIcon(
            ':/icons/icons/cil-lightbulb.png' if self.dark_theme else ':/icons/icons/cil-moon.png'))

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        text = event.mimeData().text()
        if urls:
            for url in urls:
                local_path = url.toLocalFile()
                if os.path.isdir(local_path):
                    self.media_player.select_new_folder(local_path)
                elif any(local_path.endswith(ext) for ext in
                         self.media_player.mainwindow.audio_formats + self.media_player.mainwindow.video_formats):
                    self.ui.mainAppStack.setCurrentIndex(4)
                    self.media_player.play_media_from_path(local_path)
        if text:
            youtube_url_pattern = re.compile(
                r'^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$')
            if youtube_url_pattern.match(text):
                self.ui.addDownload(text, text, self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.ui.playerOffBtn.click()
            self.ui.mainAppStack.setCurrentIndex(0)
        if event.key() == Qt.Key_Minus:
            self.setMinimized()
        if event.key() == Qt.Key_L:
            self.ui.mediaLockBtn.click()
        if not self.is_locked:
            if event.key() == Qt.Key_F and self.ui.mainAppStack.currentIndex() == 4:
                self.ui.mediaPlayBtn.click()
            if event.key() == Qt.Key_O and self.ui.mainAppStack.currentIndex() == 4:
                self.ui.videoWidgetBtn.click()
            if event.key() == Qt.Key_N and self.ui.mainAppStack.currentIndex() == 4:
                self.ui.mediaNextBtn.click()
            if event.key() == Qt.Key_P and self.ui.mainAppStack.currentIndex() == 4:
                self.ui.mediaPreviousBtn.click()
            if event.key() == Qt.Key_S and self.ui.mainAppStack.currentIndex() == 4:
                self.ui.mediaShuffleBtn.click()
            if event.key() == Qt.Key_V:
                self.ui.mediaPlayBtn.click()
            if event.key() == Qt.Key_X:
                self.ui.mediaPreviousBtn.click()
            if event.key() == Qt.Key_N:
                self.ui.mediaNextBtn.click()
            if event.key() == Qt.Key_C:
                self.ui.seekBackwardBtn.click()
            if event.key() == Qt.Key_B:
                self.ui.seekForwardBtn.click()
            if event.key() == Qt.Key_U:
                self.media_player.change_volume(5)
            if event.key() == Qt.Key_J:
                self.media_player.change_volume(-5)
            if event.key() == Qt.Key_Z:
                self.ui.fileOpenBtn.click()
            if event.key() == Qt.Key_Space:
                self.ui.mediaPlayBtn.click()
            if event.key() == Qt.Key_Up:
                self.media_player.change_volume(5)
            if event.key() == Qt.Key_Down:
                self.media_player.change_volume(-5)
            if event.key() == Qt.Key_Left:
                self.ui.seekBackwardBtn.click()
            if event.key() == Qt.Key_Right:
                self.ui.seekForwardBtn.click()
            if event.key() == Qt.Key_R:
                self.ui.mediaRepeatBtn.click()
            if event.key() == Qt.Key_E:
                self.ui.mediaShuffleBtn.click()
            if event.key() == Qt.Key_M:
                self.ui.mediaMuteBtn.click()
        if event.key() == Qt.Key_K:
            self.ui.networkBtn.click()
        if event.key() == Qt.Key_W:
            self.ui.playSoundBtn.click()
        if event.key() == Qt.Key_F:
            self.ui.mainAppStack.setCurrentIndex(4)
        if event.key() == Qt.Key_H and not self.ui.mainAppStack.currentIndex():
            self.ui.mainAppStack.setCurrentIndex(5)
        elif event.key() == Qt.Key_H:
            self.ui.mainAppStack.setCurrentIndex(0)
        if event.key() == Qt.Key_T:
            self.toggleTheme()
        if event.key() == Qt.Key_S:
            self.toggleSidebar()
        if not self.ui.mainAppStack.currentIndex() and (event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):
            self.ui.searchBtn.click()
        if self.ui.mainAppStack.currentIndex() == 3 and event.key() == Qt.Key_P:
            try:
                self.ui.downloadPause.click()
            except AttributeError:
                pass
        if self.ui.mainAppStack.currentIndex() == 3 and event.key() == Qt.Key_D:
            try:
                self.ui.downloadBtn.click()
            except AttributeError:
                pass
        if event.key() == Qt.Key_D:
            self.ui.mainAppStack.setCurrentIndex(3)

    def toggleLogger(self):
        if self.logger_visible:
            self.ui.currentInfoLabel.hide()
            self.ui.loggerBtn.setText("Disabled")
            self.logger_visible = False
            self.pushNotification("App Logs Will be Hidden")
        else:
            self.ui.currentInfoLabel.show()
            self.ui.loggerBtn.setText("Enabled")
            self.logger_visible = True
            self.pushNotification("App Logs Will be Shown")

    def redirectYouTube(self):
        webbrowser.open_new_tab("https://youtube.com")

    def redirectGithub(self):
        webbrowser.open_new_tab("https://github.com/chinmaykrishnroy/QTube")

    def redirectLinkedIn(self):
        webbrowser.open_new_tab("https://linkedin.com/in/chinmaykrishnroy")

    def redirectInstagram(self):
        webbrowser.open_new_tab("https://instagram.com/chinmaykrishnroy")

    def toggleInitialRandomSearch(self):
        self.allow_random_initial_query = not self.allow_random_initial_query
        self.ui.randInitBtn.setText(
            "Enabled" if self.allow_random_initial_query else "Disabled")
        self.pushNotification(
            "Enabled Random Search Results Upon App Launch" if self.allow_random_initial_query else "Disabled Random Search Results Upon App Launch")

    def showKitten(self):
        self.ui.loadingLabel.hide()
        self.ui.mainAppStack.setCurrentIndex(1)
        QTimer.singleShot(
            2000, lambda: self.ui.mainAppStack.setCurrentIndex(0))
        QTimer.singleShot(2000, lambda: self.ui.loadingLabel.show())

    def closeEvent(self, event):
        self.hide()
        self.saveState()
        self.playSound('%s/sound/close.mp3' % os.getcwd(), 10)
        self.media_player.cleanup_before_exit()
        try:
            self.ui.download_thread.stop()
        except AttributeError:
            print("download thread was never created")
        try:
            self.ui.stopImageDownloaderThreads()
        except AttributeError:
            print("image downloader thread was never created")
        try:
            self.search_thread.stop()
        except AttributeError:
            print("search thread was never created")
        self.timer.stop()
        self.dots_timer.stop()
        self.internet_checker.stop()
        self.internet_checker.join()
        self.file_watcher_system.stop()
        self.close()
        event.accept()
