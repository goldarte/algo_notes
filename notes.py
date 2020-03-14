import os
import sys
import json
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QInputDialog, QLineEdit, QMessageBox
from PyQt5 import QtCore
from notes_gui import Ui_MainWindow

notes = {}

def show_error_msg(msg):
    error_msg = QMessageBox()
    error_msg.setIcon(QMessageBox.Critical)
    error_msg.setWindowTitle('Ошибка!')
    error_msg.setText(msg)
    error_msg.exec_()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.addNoteButton.clicked.connect(self.add_note)
        self.ui.removeNoteButton.clicked.connect(self.remove_note)
        self.ui.saveNoteButton.clicked.connect(self.save_note)
        self.ui.notesListWidget.itemClicked.connect(self.update_text)
        self.ui.notesListWidget.itemSelectionChanged.connect(self.update_text)
        self.ui.saveNotesAction.triggered.connect(self.save_notes)

    def add_note(self):
        text, ok = QInputDialog().getText(self, "Добавить заметку", "Название заметки: ")
        if ok and text:
            if not text in notes.keys():
                notes[text] = {}
                notes[text]["text"] = ""
                notes[text]["tags"] = []
                self.ui.notesListWidget.addItem(text)
                self.ui.notesListWidget.findItems(text, QtCore.Qt.MatchExactly)[0].setSelected(True)
                print(notes)
            else:
                show_error_msg('Такая заметка уже есть! Введите другое имя.')

    def remove_note(self):
        if self.ui.notesListWidget.selectedItems():
            current_item = self.ui.notesListWidget.selectedItems()[0]
            index = self.ui.notesListWidget.row(current_item)
            self.ui.notesListWidget.takeItem(index)
            del notes[current_item.text()]
            print(notes)
        else:
            print("Не выбран элемент!")

    def save_note(self):
        if self.ui.notesListWidget.selectedItems():
            key = self.ui.notesListWidget.selectedItems()[0].text()
            notes[key]["text"] = self.ui.noteTextEdit.toPlainText()
            print(notes)
        else:
            print("Не выбран элемент!")

    def update_text(self):
        if self.ui.notesListWidget.selectedItems():
            key = self.ui.notesListWidget.selectedItems()[0].text()
            self.ui.noteTextEdit.setText(notes[key]["text"])

    def save_notes(self):
        save_path = QFileDialog.getSaveFileName(self, "Сохранить файл с заметками",
                                                directory='notes.json',
                                                filter="json files (*.json)")[0]
        split_path = save_path.split('.')

        if not (len(split_path) > 1 and split_path[-1] == 'json'):
            save_path += '.json'

        with open(save_path, "w") as write_file:
            json.dump(notes, write_file)
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()