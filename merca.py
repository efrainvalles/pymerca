import PyQt5
import sys
from PyQt5.QtWidgets import QButtonGroup, QMenu, QMainWindow, QApplication, QWidget, QCompleter, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, QTimer, QUrl
from PyQt5.QtWebEngine import *
from PyQt5.QtWebEngineWidgets import *

##import lib.docol as docol
import os
import re
import subprocess
from melisdk import Meli  

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
        self.height = 540
        self.setFixedSize(self.width, self.height)
        self.initUI()
    
    def initUI(self):
        menubar = self.menuBar()
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')
        viewMenu = menubar.addMenu('View')
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        appmenu = menubar.addMenu('File')
        impMenu = QMenu('Import', self)
        impAct = QAction('Import Mail', self)
        viewMenu.addAction(viewStatAct)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('img.png'))
        pixmap1 = QPixmap("img.png")
        self.logo = QLabel(self)
        self.logo.resize(200,113)
        self.logo.setPixmap(pixmap1)
        self.logo.move(20,20)

        self.lbl = QLabel(self)
        self.lbl.resize(50,30)
        self.lbl.move(20,140)
        self.lbl.setText("1 - Client ID")

        self.tBox = QLineEdit(self)
        self.tBox.move(100,140)
        self.tBox.resize(360,30)
        self.tBox.setText('4488546561358677') #test



        self.lbl2 = QLabel(self)
        self.lbl2.resize(80,30)
        self.lbl2.move(20,180)
        self.lbl2.setText("2 - Client Secret")


        self.tBox2 = QLineEdit(self)
        self.tBox2.move(100,180)
        self.tBox2.resize(360,30)
        self.tBox2.setText('qujfaJroZ5YLGRIsP3wIfDp5jVJwdWZS') #test
        self.tBox2.setStyleSheet('QLabel { border-radius:5px;  border: 2px solid green; color: orange;border-radius: 3px;font-size:22px}')


        self.lbl3 = QLabel(self)
        self.lbl3.resize(120,30)
        self.lbl3.move(20,220)
        self.lbl3.setText("3 - Redirect URI")

        self.tBox3 = QLineEdit(self)
        self.tBox3.move(100,220)
        self.tBox3.resize(360,30)
        self.tBox3.setStyleSheet('QLabel { border-radius:5px;  border: 2px solid green; color: orange;border-radius: 3px;font-size:22px}')
        self.tBox3.setText('https://effguitar.rocks') #test
        self.tBox3.textChanged.connect(self.checkReadiness)
        self.tBox.textChanged.connect(self.checkReadiness)
        self.tBox2.textChanged.connect(self.checkReadiness)

        self.lbl4 = QLabel(self)
        self.lbl4.resize(160,30)
        self.lbl4.move(20,260)
        self.lbl4.setText("4 - Redirect URL")

        self.tBox4 = QLineEdit(self)
        self.tBox4.move(100,260)
        self.tBox4.resize(360,30)
        self.tBox4.setStyleSheet('QLabel { border-radius:5px;  border: 2px solid green; color: orange;border-radius: 3px;font-size:22px}')

        self.lbl5 = QLabel(self)
        self.lbl5.resize(160,30)
        self.lbl5.move(20,300)
        self.lbl5.setText("5 - Code")


        self.tBox5 = QLineEdit(self)
        self.tBox5.move(100,300)
        self.tBox5.resize(360,30)
        self.tBox5.setStyleSheet('QLabel { border-radius:5px;  border: 2px solid green; color: orange;border-radius: 3px;font-size:22px}')

        self.lbl6 = QLabel(self)
        self.lbl6.resize(160,30)
        self.lbl6.move(20,340)
        self.lbl6.setText("6 - Token")

        self.tBox6 = QLineEdit(self)
        self.tBox6.move(100,340)
        self.tBox6.resize(360,30)
        self.tBox6.setStyleSheet('QLabel { border-radius:5px;  border: 2px solid green; color: orange;border-radius: 3px;font-size:22px}')

        self.tBox5.textChanged.connect(self.activate_getToken)

        self.bttn = QPushButton('Solicitar Auth',self)
        self.bttn.move(470,140)
        self.bttn.setStyleSheet('QPushButton { background-color:#545454; color: white;border-radius: 3px;font-size:14px}')
        self.bttn.resize(105,70)
        self.bttn.setDisabled(True)

        self.bttn2 = QPushButton('Solicitar Token',self)
        self.bttn2.move(470,220)
        self.bttn2.resize(105,70)
        self.bttn2.setStyleSheet('QPushButton { background-color:#545454; color: white;border-radius: 3px;font-size:14px}')
        self.bttn2.setDisabled(True)
        self.bttn2.clicked.connect(self.getToken)

        self.btn_grp = QButtonGroup()
        self.btn_grp.setExclusive(True)
        self.btn_grp.addButton(self.bttn)
        self.btn_grp.buttonClicked.connect(self.getAuth)
        self.show()

        self.testit = website(self)
        self.testit.browser.urlChanged.connect(self.printit)

    @pyqtSlot()

    def printit(self):
        urlInText=self.testit.browser.url().toString()
        print(urlInText)
        if urlInText.startswith(self.tBox3.text()):
            code = urlInText.split('?code=')
            print(code)
            self.tBox5.setText(code[1])
            self.testit.hide()
            self.getToken()



    def generateAPI(self):
        mi=docol.makeit()
        done=mi.processit(self.textbox2.text(),self.textbox.text())
        self.statusbar.showMessage(done)
        self.textbox6.setText(done) 


    def getToken(self):
        if self.tBox5.text is not '':
            meli = Meli(client_id=int(self.tBox.text()), client_secret=self.tBox2.text())
            token=meli.authorize(code=self.tBox5.text(), redirect_URI=self.tBox3.text())
            self.tBox6.setText(token)
            return token
        else:
            QMessageBox.information(self, 'No Hay Codigo : Code', 'No Hya code, copie y pegue desde la pagina', QMessageBox.Ok, QMessageBox.Ok)

    def getAuth(self):
        ready = self.checkReadiness()
        if ready == True:
            meli = Meli(client_id=int(self.tBox.text()), client_secret=self.tBox2.text())
            redirectURI=meli.auth_url(redirect_URI=self.tBox3.text())
            self.tBox4.setText(redirectURI)
            self.testit.browser.setUrl(QUrl(self.tBox4.text()))
            self.testit.show() 
            self.activate_getToken()
        else: 
            QMessageBox.information(self, 'Try Again', "Llene los datos otra vez", QMessageBox.Ok, QMessageBox.Ok)


    def checkReadiness(self):
        tboxValue = self.tBox.text()
        tbox2Value = self.tBox2.text()
        tbox3Value = self.tBox3.text()
        if tboxValue is not '' and tbox2Value is not '' and tbox3Value is not '' :
            self.bttn.setDisabled(False)
            self.bttn.setStyleSheet('QPushButton { background-color:#4ec25b; color: white;border-radius: 3px;font-size:14px;font-weight: 400}')

            return True
        else: 
            self.bttn.setStyleSheet('QPushButton { background-color:#545454; color: white;border-radius: 3px;font-size:14px}')
            self.bttn.setDisabled(True)
            return False

    def activate_getToken(self):
        ready = self.checkReadiness()
        if ready == True and self.tBox4.text is not '' and self.tBox5.text is not '':
            self.bttn2.setDisabled(False)
            self.bttn2.setStyleSheet('QPushButton { background-color:#4ec25b; color: white;border-radius: 3px;font-size:14px;font-weight: 400}')

    def validate_text2(self):
        mi = docol.makeit()
        textboxValue2 = self.textbox2.text()
        if not textboxValue2.endswith(".csv"):
            QMessageBox.information(self, 'No es un CSV', "No es un CSV, revise que sea un APIS report de Airline Choice  %s" % (textboxValue2), QMessageBox.Ok, QMessageBox.Ok)
            self.statusbar.showMessage("El Archivo no es un CSV")
            self.textbox2.setText("")
        else:
            self.label4.setText(mi.get_flight_info(self.textbox2.text())) 
            self.activate_generate()
            if mi.checkdates() == "warning":
                QMessageBox.information(self, 'Fechas no cuadran', 'Fechas no cuadran', QMessageBox.Ok, QMessageBox.Ok)
        return

    def on_click(self):
        print (self)
        textboxValue = self.textbox.text()
        find_vendor = self.checkandsearch()
        if not find_vendor:
            QMessageBox.information(self, 'No Records', "No Result", QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.information(self, 'La agencia es', "Es: " + find_vendor[0].name, QMessageBox.Ok, QMessageBox.Ok)
            self.label1.setText("Busqueda:" + textboxValue)
            self.label2.setText("Email:" + find_vendor[0].email)
            self.label3.setText("Agencia:" + find_vendor[0].name)
            self.textbox.setText("")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.checkReadiness()
    sys.exit(app.exec_())