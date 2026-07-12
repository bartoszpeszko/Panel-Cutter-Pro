from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
)

from PySide6.QtCore import Qt
from core.services.image_loader import ImageLoader

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Panel Cutter Pro")
        self.resize(900, 650)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()

        title = QLabel("📸 Panel Cutter Pro")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            padding:20px;
        """)

        layout.addWidget(title)

        self.button = QPushButton("📂 Wybierz obraz")

        self.button.setMinimumHeight(60)

        self.button.clicked.connect(self.open_image)

        layout.addWidget(self.button)

        self.info = QLabel(
            "Przeciągnij obraz tutaj\n\nlub kliknij przycisk."
        )

        self.info.setAlignment(Qt.AlignCenter)

        self.info.setStyleSheet("""
            border:3px dashed gray;
            border-radius:10px;
            font-size:18px;
            padding:80px;
        """)

        layout.addWidget(self.info)

        self.status = QLabel("Gotowy.")

        layout.addWidget(self.status)

        central.setLayout(layout)

    def open_image(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Wybierz obraz",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )

        if not filename:
            return

        loader = ImageLoader()

        try:
            data = loader.load(filename)

            self.info.setText(
                f"""📄 Plik:
    {data["filename"]}

    📐 Rozdzielczość:
    {data["width"]} × {data["height"]}

    🖼 Orientacja:
    {data["orientation"]}
    """
            )

            self.status.setText("Obraz został poprawnie wczytany.")

        except Exception as e:
            self.status.setText(str(e))