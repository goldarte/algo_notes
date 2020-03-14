import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication
from notes_gui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()