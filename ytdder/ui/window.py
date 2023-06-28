from pathlib import Path
from PyQt6.uic.load_ui import loadUi
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QLineEdit, QPushButton, QListView

here = Path(__file__).parent


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(here / "main.ui", self)
        self.url: QLineEdit
        self.url.setPlaceholderText("YouTube video URL")  # type: ignore
        self.button_dn: QPushButton
        self.button_dn.clicked.connect(self.download)  # type: ignore
        self.button_check: QPushButton
        self.button_check.clicked.connect(self.check_link)  # type: ignore
        self.streams_list: QListView

    def download(self) -> None:
        print("Downloading...")

    def check_link(self) -> None:
        link = self.url.text()
        print("Checking link validity...")
        print(f"Link is: {link}")

    def get_filename(self) -> None:
        file_name = QFileDialog.getSaveFileName(self, "Save file", str(Path.home()))
        print(file_name)
