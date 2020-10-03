import PyQt5
import sys
from PyQt5.QtWidgets import QButtonGroup, QMenu, QMainWindow, QApplication, QWidget, QCompleter, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, QTimer, QUrl
from PyQt5.QtWebEngine import *
from PyQt5.QtWebEngineWidgets import *


class website(QMainWindow):
 def __init__(self, parent=None):
        super(website, self).__init__(parent)


        self.left = 300
        self.top = 200
        self.width = 800
        self.height = 650
        self.setFixedSize(self.width, self.height)

        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)



class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = " Generar Token para MercadoLibre.com"
        self.left = 800
        self.top = 200
        self.width = 600
        self.height = 450
        self.setFixedSize(self.width, self.height)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.lbl = QLabel(self)
        self.lbl.resize(50,30)
        self.lbl.move(20,140)
        self.lbl.setText("1 - URL")

        self.tBox = QLineEdit(self)
        self.tBox.move(100,140)
        self.tBox.resize(360,30)
        self.tBox.setText('http://google.com') 

        self.bttn = QPushButton('Enviar URL',self)
        self.bttn.move(470,220)
        self.bttn.resize(105,70)
        self.bttn.setStyleSheet('QPushButton { background-color:#545454; color: white;border-radius: 3px;font-size:14px}')

        self.bttn.clicked.connect(self.sendArg)

        self.testit = website(self)
        self.testit.browser.urlChanged.connect(self.printit)

        self.show()

    @pyqtSlot()
    

    def sendArg(self):
        self.testit.browser.setUrl(QUrl(self.tBox.text()))
        self.testit.show() 

    def printit(self):
        print(self.testit.browser.url())




        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())