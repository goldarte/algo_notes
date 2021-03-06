# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notes_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 714)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.noteTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.noteTextEdit.setGeometry(QtCore.QRect(10, 10, 641, 671))
        self.noteTextEdit.setObjectName("noteTextEdit")
        self.addTagButton = QtWidgets.QPushButton(self.centralwidget)
        self.addTagButton.setGeometry(QtCore.QRect(660, 620, 101, 27))
        self.addTagButton.setObjectName("addTagButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 10, 131, 17))
        self.label.setObjectName("label")
        self.removeTagButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeTagButton.setGeometry(QtCore.QRect(760, 620, 101, 27))
        self.removeTagButton.setObjectName("removeTagButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 420, 131, 17))
        self.label_2.setObjectName("label_2")
        self.searchTagButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchTagButton.setGeometry(QtCore.QRect(660, 650, 201, 27))
        self.searchTagButton.setObjectName("searchTagButton")
        self.addNoteButton = QtWidgets.QPushButton(self.centralwidget)
        self.addNoteButton.setGeometry(QtCore.QRect(660, 350, 101, 27))
        self.addNoteButton.setObjectName("addNoteButton")
        self.removeNoteButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeNoteButton.setGeometry(QtCore.QRect(760, 350, 101, 27))
        self.removeNoteButton.setObjectName("removeNoteButton")
        self.saveNoteButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveNoteButton.setGeometry(QtCore.QRect(660, 380, 201, 27))
        self.saveNoteButton.setObjectName("saveNoteButton")
        self.tagLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.tagLineEdit.setGeometry(QtCore.QRect(660, 580, 201, 31))
        self.tagLineEdit.setObjectName("tagLineEdit")
        self.notesListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.notesListWidget.setGeometry(QtCore.QRect(660, 30, 201, 311))
        self.notesListWidget.setObjectName("notesListWidget")
        self.tagsListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.tagsListWidget.setGeometry(QtCore.QRect(660, 440, 201, 131))
        self.tagsListWidget.setObjectName("tagsListWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.newNotesAction = QtWidgets.QAction(MainWindow)
        self.newNotesAction.setObjectName("newNotesAction")
        self.saveNotesAction = QtWidgets.QAction(MainWindow)
        self.saveNotesAction.setObjectName("saveNotesAction")
        self.openNotesAction = QtWidgets.QAction(MainWindow)
        self.openNotesAction.setObjectName("openNotesAction")
        self.actionOpen_and_edit = QtWidgets.QAction(MainWindow)
        self.actionOpen_and_edit.setObjectName("actionOpen_and_edit")
        self.actionBy_Name = QtWidgets.QAction(MainWindow)
        self.actionBy_Name.setObjectName("actionBy_Name")
        self.actionBy_Tag = QtWidgets.QAction(MainWindow)
        self.actionBy_Tag.setObjectName("actionBy_Tag")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menuFile.addAction(self.newNotesAction)
        self.menuFile.addAction(self.openNotesAction)
        self.menuFile.addAction(self.saveNotesAction)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addTagButton.setText(_translate("MainWindow", "Добавить"))
        self.label.setText(_translate("MainWindow", "Список заметок"))
        self.removeTagButton.setText(_translate("MainWindow", "Удалить"))
        self.label_2.setText(_translate("MainWindow", "Теги заметки"))
        self.searchTagButton.setText(_translate("MainWindow", "Поиск по тегу"))
        self.addNoteButton.setText(_translate("MainWindow", "Добавить"))
        self.removeNoteButton.setText(_translate("MainWindow", "Удалить"))
        self.saveNoteButton.setText(_translate("MainWindow", "Сохранить"))
        self.tagLineEdit.setPlaceholderText(_translate("MainWindow", "Введите тег..."))
        self.menuFile.setTitle(_translate("MainWindow", "Заметки"))
        self.newNotesAction.setText(_translate("MainWindow", "Создать"))
        self.saveNotesAction.setText(_translate("MainWindow", "Сохранить"))
        self.openNotesAction.setText(_translate("MainWindow", "Открыть..."))
        self.actionOpen_and_edit.setText(_translate("MainWindow", "Open and edit"))
        self.actionBy_Name.setText(_translate("MainWindow", "По имени"))
        self.actionBy_Tag.setText(_translate("MainWindow", "По тегу"))
        self.action.setText(_translate("MainWindow", "По дате создания"))
        self.action_2.setText(_translate("MainWindow", "Выбрать рабочую папку..."))
