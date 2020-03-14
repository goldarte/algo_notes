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
        self.ui.notesListWidget.itemClicked.connect(self.note_select)
        self.ui.notesListWidget.itemSelectionChanged.connect(self.note_select)
        self.ui.saveNotesAction.triggered.connect(self.save_notes)
        self.ui.openNotesAction.triggered.connect(self.open_notes)
        self.ui.newNotesAction.triggered.connect(self.create_new_note)
        self.ui.addTagButton.clicked.connect(self.add_tag)
        self.ui.removeTagButton.clicked.connect(self.remove_tag)
        self.ui.searchTagButton.clicked.connect(self.search_tag)
        self.ui.tagsListWidget.itemClicked.connect(self.tag_select)

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

    def note_select(self):
        if self.ui.notesListWidget.selectedItems():
            key = self.ui.notesListWidget.selectedItems()[0].text()
            self.ui.noteTextEdit.setText(self.notes[key]['text'])
            self.ui.tagsListWidget.clear()
            if self.notes[key]['tags']:
                self.ui.tagsListWidget.addItems(self.notes[key]['tags'])

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

    def set_ui(self, input_notes):
        self.ui.notesListWidget.clear()
        self.ui.noteTextEdit.clear()
        self.ui.tagsListWidget.clear()
        if input_notes:
            self.ui.notesListWidget.addItems(input_notes.keys())
            self.ui.notesListWidget.itemAt(0, 0).setSelected(True)

    def add_tag(self):
        if self.ui.notesListWidget.selectedItems():
            key = self.ui.notesListWidget.selectedItems()[0].text()
            tag = self.ui.tagLineEdit.text()
            if tag:
                if not tag in self.notes[key]['tags']:
                    self.notes[key]['tags'].append(tag)
                    self.ui.tagsListWidget.addItem(tag)
                    self.ui.tagsListWidget.findItems(tag, QtCore.Qt.MatchExactly)[0].setSelected(True)
                    print(self.notes)
        else:
            print('Не выбран элемент!')

    def remove_tag(self):
        if self.ui.notesListWidget.selectedItems():
            key = self.ui.notesListWidget.selectedItems()[0].text()
            if self.ui.tagsListWidget.selectedItems():
                tag_item = self.ui.tagsListWidget.selectedItems()[0]
                tag_item_index = self.ui.tagsListWidget.row(tag_item)
                tag_note_index = self.notes[key]['tags'].index(tag_item.text())
                self.ui.tagsListWidget.takeItem(tag_item_index)
                del self.notes[key]['tags'][tag_note_index]
                print(self.notes)
        else:
            print("Не выбран элемент!")

    def tag_select(self):
        if self.ui.tagsListWidget.selectedItems():
            tag = self.ui.tagsListWidget.selectedItems()[0].text()
            self.ui.tagLineEdit.setText(tag)

    def search_tag(self):
        tag = self.ui.tagLineEdit.text()
        notes_filtered = {}
        for note in self.notes:
            if not tag or tag in self.notes[note]['tags']:
                notes_filtered[note] = self.notes[note]
        if notes_filtered:
            self.set_ui(notes_filtered)
        else:
            show_error_msg("Такого тега в заметках нет!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()