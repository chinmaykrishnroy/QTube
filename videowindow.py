from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QMainWindow


class VideoWindow(QMainWindow):
    def __init__(self, ui, media_player):
        super().__init__()
        self.ui = ui
        self.media_player = media_player
        self.setWindowIcon(QIcon(':/icons/PyPlayer.ico'))
        self.setWindowTitle("PyPlayer")
        self.setGeometry(100, 100, 1280, 720)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.video_widget = QVideoWidget()
        self.setCentralWidget(self.video_widget)
        self.is_fullscreen = False
        self.video_widget.mouseDoubleClickEvent = self.toggle_fullscreen
        self.offset = None

    def toggle_fullscreen(self, event):
        if self.is_fullscreen:
            self.showNormal()
            self.unsetCursor()
        else:
            self.showFullScreen()
            self.setCursor(Qt.BlankCursor)
        self.is_fullscreen = not self.is_fullscreen

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event):
        self.offset = None

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F:
            self.toggle_fullscreen(event)
        if event.key() == Qt.Key_Escape and self.is_fullscreen:
            self.toggle_fullscreen(event)
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
        if event.key() == Qt.Key_O:
            self.ui.videoWidgetBtn.click()
        super().keyPressEvent(event)

    def closeEvent(self, event):
        if self.media_player.is_video:
            self.ui.videoWidgetBtn.click()
        event.accept()
