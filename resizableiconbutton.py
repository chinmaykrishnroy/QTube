from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton, QSizePolicy


class ResizableIconButton(QPushButton):
    def __init__(self, text='', *args, **kwargs):
        super().__init__(text, *args, **kwargs)
        self.icon_path = None
        self.current_icon = None
        self.setMinimumSize(360, 202)
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        button_size = self.size()
        button_size = button_size.boundedTo(QSize(640, 360))
        self.updateIconSize(button_size)

    def updateIconSize(self, size):
        if self.current_icon:
            pixmap = self.current_icon.pixmap(size)
            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(
                    size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                super().setIcon(QIcon(scaled_pixmap))
                self.setIconSize(size)

    def setIcon(self, icon):
        if isinstance(icon, str):
            self.icon_path = icon
            pixmap = QPixmap(self.icon_path)
            self.current_icon = QIcon(pixmap)
        elif isinstance(icon, QIcon):
            self.current_icon = icon
        else:
            raise ValueError("Icon must be a file path or a QIcon instance.")

        button_size = self.size()
        self.updateIconSize(button_size)

    def setIconFromData(self, data):
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        icon = QIcon(pixmap)
        self.setIcon(icon)
