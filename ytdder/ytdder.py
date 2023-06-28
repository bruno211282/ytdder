from PyQt6.QtWidgets import QApplication
from ui.window import Window


def main():
    app = QApplication([])
    win = Window()
    win.show()
    app.exec()


if __name__ == "__main__":
    main()
