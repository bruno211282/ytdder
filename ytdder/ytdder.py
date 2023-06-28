from pathlib import Path
from PyQt6.uic.load_ui import loadUi
from PyQt6.QtWidgets import QApplication, QWidget

here = Path(__file__).parent


def main():
    app = QApplication([])
    win: QWidget = loadUi(here / "ui" / "main.ui")  # type: ignore
    win.show()
    app.exec()


if __name__ == "__main__":
    main()
