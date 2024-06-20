from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtWidgets import QLabel


class ElidedLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.original_text = ""
        self.setSizePolicy(self.sizePolicy().horizontalPolicy(), self.sizePolicy().verticalPolicy())
        self.setWordWrap(False)  # Ensure text does not wrap to the next line
        self.setFixedHeight(16)  # Set a fixed height for the QLabel to ensure single-line display
        if parent is not None:
            parent.installEventFilter(self)  # Install an event filter on the parent

    def setText(self, text):
        self.original_text = text
        self.updateText()

    def eventFilter(self, source, event):
        if event.type() == QEvent.Resize and source is self.parent():
            self.updateText()
        return super().eventFilter(source, event)

    def resizeEvent(self, event):
        self.updateText()
        super().resizeEvent(event)

    def updateText(self):
        if self.parent() is not None:
            width = self.parent().width() - 10  # Slightly reduce width to account for padding
            elided_text = self.elidedText(self.original_text, width)
            super().setText(elided_text)

    def elidedText(self, text, width):
        metrics = QFontMetrics(self.font())
        return metrics.elidedText(text, Qt.ElideRight, width)


class ElidedLabel2(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.original_text = ""
        self.setSizePolicy(self.sizePolicy().horizontalPolicy(), self.sizePolicy().verticalPolicy())
        self.setWordWrap(False)
        if parent is not None:
            parent.installEventFilter(self)

    def setText(self, text):
        self.original_text = text
        self.updateText()

    def eventFilter(self, source, event):
        if event.type() == QEvent.Resize and source is self.parent():
            self.updateText()
        return super().eventFilter(source, event)

    def resizeEvent(self, event):
        self.updateText()
        super().resizeEvent(event)

    def updateText(self):
        if self.parent() is not None:
            width = self.parent().width() - 10
            elided_text = self.elidedText(self.original_text, width)
            super().setText(elided_text)

    def elidedText(self, text, width):
        metrics = QFontMetrics(self.font())
        return metrics.elidedText(text, Qt.ElideRight, width)
