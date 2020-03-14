import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QInputDialog, QLineEdit
from notes_gui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.addNoteButton.clicked.connect(self.add_note)

    def add_note(self):
        text, ok = QInputDialog.getText(self, "Добавить заметку",
                                        "Название заметки: ")
        if ok and text:
            print(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()