from PyQt5.QtCore import QSize, QRectF, QPoint, QRect
from PyQt5.QtGui import QPainter, QPainterPath
from PyQt5.QtWidgets import QPushButton


class CircularIconButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(CircularIconButton, self).__init__(*args, **kwargs)
        self._icon = None
        self._icon_size = QSize(24, 24)  # Default icon size

    def setIcon(self, icon):
        self._icon = icon
        self.update()

    def icon(self):
        return self._icon

    def setIconSize(self, size):
        self._icon_size = size
        self.update()

    def iconSize(self):
        return self._icon_size

    def paintEvent(self, event):
        super(CircularIconButton, self).paintEvent(event)

        if self._icon:
            painter = QPainter(self)
            rect = QRect(QPoint(0, 0), self._icon_size)
            rect.moveCenter(self.rect().center())

            # Draw the circular clipping region
            path = QPainterPath()
            path.addEllipse(QRectF(rect))

            painter.setClipPath(path)
            pixmap = self._icon.pixmap(self._icon_size)
            painter.drawPixmap(rect, pixmap)
            painter.end()
