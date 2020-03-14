import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QInputDialog, QLineEdit, QMessageBox
from notes_gui import Ui_MainWindow

notes = {}

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.addNoteButton.clicked.connect(self.add_note)
        self.ui.removeNoteButton.clicked.connect(self.remove_note)

    def add_note(self):
        text, ok = QInputDialog().getText(self, "Добавить заметку",
                                        "Название заметки: ")
        if ok and text:
            if not text in notes.keys():
                notes[text] = ""
                self.ui.notesListWidget.addItem(text)
                print(notes)
            else:
                error_msg = QMessageBox()
                error_msg.setIcon(QMessageBox.Critical)
                error_msg.setWindowTitle('Ошибка!')
                error_msg.setText('Такая заметка уже есть! Введите другое имя.')
                error_msg.exec_()

    def remove_note(self):
        if self.ui.notesListWidget.selectedItems():
            current_item = self.ui.notesListWidget.currentItem()
            index = self.ui.notesListWidget.row(current_item)
            self.ui.notesListWidget.takeItem(index)
            del notes[current_item.text()]
            print(notes)
        else:
            print("Не выбран элемент!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()