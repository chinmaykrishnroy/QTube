import requests
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton


class ImageDownloader(QThread):
    imageDownloaded = pyqtSignal(QPixmap, QPushButton)

    def __init__(self, url, button):
        super().__init__()
        self.url = url
        self.button = button
        self._is_running = True

    def run(self):
        if not self._is_running:
            return
        response = requests.get(self.url)
        if not self._is_running:
            return
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        if self._is_running:
            self.imageDownloaded.emit(pixmap, self.button)

    def stop(self):
        self._is_running = False
