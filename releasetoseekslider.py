from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider


class SeekSlider(QSlider):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            value = self.minimum() + ((self.maximum() - self.minimum())
                                      * event.x()) / self.width()
            self.setValue(int(value))
            self.sliderMoved.emit(int(value))
        super().mousePressEvent(event)

    def wheelEvent(self, event):
        delta = event.angleDelta().y()
        step = 1
        if delta > 0: self.setValue(self.value() + step)
        else: self.setValue(self.value() - step)
        self.sliderMoved.emit(self.value())
        super().wheelEvent(event)