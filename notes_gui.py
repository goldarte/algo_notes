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
        MainWindow.resize(874, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 641, 561))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(660, 350, 201, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 390, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(660, 30, 201, 311))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 10, 131, 17))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(760, 390, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(660, 490, 201, 81))
        self.listView_2.setObjectName("listView_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 470, 131, 17))
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 420, 201, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
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
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "Введите тег..."))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.label.setText(_translate("MainWindow", "Список заметок"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить"))
        self.label_2.setText(_translate("MainWindow", "Теги заметки"))
        self.pushButton_3.setText(_translate("MainWindow", "Поиск по тегу"))
        self.menuFile.setTitle(_translate("MainWindow", "Заметка"))
        self.menu.setTitle(_translate("MainWindow", "Настройки"))
        self.actionNew.setText(_translate("MainWindow", "Создать"))
        self.actionSave.setText(_translate("MainWindow", "Сохранить..."))
        self.actionOpen.setText(_translate("MainWindow", "Открыть..."))
        self.actionOpen_and_edit.setText(_translate("MainWindow", "Open and edit"))
        self.actionBy_Name.setText(_translate("MainWindow", "По имени"))
        self.actionBy_Tag.setText(_translate("MainWindow", "По тегу"))
        self.action.setText(_translate("MainWindow", "По дате создания"))
        self.action_2.setText(_translate("MainWindow", "Выбрать рабочую папку..."))
