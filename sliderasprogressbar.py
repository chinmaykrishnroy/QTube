from PyQt5.QtWidgets import QSlider


class ProgressbarSlider(QSlider):
    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        event.ignore()

    def mouseMoveEvent(self, event):
        event.ignore()

    def mouseReleaseEvent(self, event):
        event.ignore()

    def keyPressEvent(self, event):
        event.ignore()
