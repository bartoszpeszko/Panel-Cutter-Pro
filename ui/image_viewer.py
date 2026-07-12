from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class ImageViewer(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText("Brak obrazu")

        self.setStyleSheet("""
            QLabel {
                background: white;
                border:1px solid #b0b0b0;
            }
        """)

    def load_image(self, filename):
        pixmap = QPixmap(filename)

        if pixmap.isNull():
            return

        pixmap = pixmap.scaled(
            self.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.setPixmap(pixmap)

    def resizeEvent(self, event):
        if self.pixmap() is not None:
            self.setPixmap(
                self.pixmap().scaled(
                    self.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )

        super().resizeEvent(event)