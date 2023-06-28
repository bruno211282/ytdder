from pathlib import Path
from PyQt6.uic.load_ui import loadUi
from PyQt6.QtWidgets import QMainWindow

here = Path(__file__).parent


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(here / "main.ui", self)

        self.button_dn.clicked.connect(self.download)  # type: ignore
        self.button_check.clicked.connect(self.check_link)  # type: ignore

    def download(self) -> None:
        print("Downloading...")

    def check_link(self) -> None:
        print("Checking link validity...")
