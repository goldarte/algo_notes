import os
import sys
import json
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QInputDialog, QLineEdit, QMessageBox
from PyQt5 import QtCore
from notes_gui import Ui_MainWindow

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
        self.notes = {}

    def init_ui(self):
        self.ui.addNoteButton.clicked.connect(self.add_note)
        self.ui.removeNoteButton.clicked.connect(self.remove_note)
        self.ui.saveNoteButton.clicked.connect(self.save_note)
        self.ui.notesListWidget.itemClicked.connect(self.update_text)
        self.ui.notesListWidget.itemSelectionChanged.connect(self.update_text)
        self.ui.saveNotesAction.triggered.connect(self.save_notes)
        self.ui.openNotesAction.triggered.connect(self.open_notes)
        self.ui.newNotesAction.triggered.connect(self.create_new_note)

    def add_note(self):
        text, ok = QInputDialog().getText(self, "Добавить заметку", "Название заметки: ")
        if ok and text:
            if not text in self.notes.keys():
                self.notes[text] = {}
                self.notes[text]['text'] = ''
                self.notes[text]['tags'] = []
                self.ui.notesListWidget.addItem(text)
                self.ui.notesListWidget.findItems(text, QtCore.Qt.MatchExactly)[0].setSelected(True)
                print(self.notes)
            else:
                show_error_msg('Такая заметка уже есть! Введите другое имя.')

    def remove_note(self):
        if self.ui.notesListWidget.selectedItems():
            current_item = self.ui.notesListWidget.selectedItems()[0]
            index = self.ui.notesListWidget.row(current_item)
            self.ui.notesListWidget.takeItem(index)
            del self.notes[current_item.text()]
            print(self.notes)
        else:
            print("Не выбран элемент!")

    def save_note(self):
        if self.ui.notesListWidget.selectedItems():
            key = self.ui.notesListWidget.selectedItems()[0].text()
            self.notes[key]["text"] = self.ui.noteTextEdit.toPlainText()
            print(self.notes)
        else:
            print("Не выбран элемент!")

    def update_text(self):
        if self.ui.notesListWidget.selectedItems():
            key = self.ui.notesListWidget.selectedItems()[0].text()
            self.ui.noteTextEdit.setText(self.notes[key]['text'])

    def save_notes(self):
        save_path = QFileDialog.getSaveFileName(self, "Сохранить файл с заметками",
                                                directory='notes.json',
                                                filter="Заметки (*.json)")[0]

        if not save_path:
            return
        
        split_path = save_path.split('.')

        if not (len(split_path) > 1 and split_path[-1] == 'json'):
            save_path += '.json'

        with open(save_path, "w") as write_file:
            json.dump(self.notes, write_file)
        
    def open_notes(self):
        path = QFileDialog.getOpenFileName(self, "Открыть файл с заметками",
                                           filter="Заметки (*.json)")[0]

        if not path:
            return

        with open(path, "r") as read_file:
            self.notes = json.load(read_file)
        
        print(self.notes)

        self.set_ui(self.notes)

    def create_new_note(self):
        self.notes = {}
        self.set_ui(self.notes)

    def set_ui(self, notes):
        self.ui.notesListWidget.clear()
        self.ui.noteTextEdit.clear()
        self.ui.tagsListWidget.clear()
        if self.notes:
            self.ui.notesListWidget.addItems(self.notes.keys())
            self.ui.notesListWidget.itemAt(0, 0).setSelected(True)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()