from PyQt5 import QtWidgets
import sys
from xx import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_toplama.clicked.connect(self.hesapla)
        self.ui.btn_cikarma.clicked.connect(self.hesapla)
        self.ui.btn_carpma.clicked.connect(self.hesapla)
        self.ui.btn_bolme.clicked.connect(self.hesapla)

    def hesapla(self):
        sender = self.sender().text()
        result = 0

        if sender == 'Topla':
            result = int(self.ui.txt_sayi1.text()) + int(self.ui.txt_sayi2.text())
        elif sender == 'Çıkar':
            result = int(self.ui.txt_sayi1.text()) - int(self.ui.txt_sayi2.text())
        elif sender == 'Çarp':
            result = int(self.ui.txt_sayi1.text()) * int(self.ui.txt_sayi2.text())
        elif sender == 'Böl':
            result = int(self.ui.txt_sayi1.text()) / int(self.ui.txt_sayi2.text())

        self.ui.lbl_sonuc.setText('sonuç: '+ str(result))


def app():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("QPushButton { color: red}")
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()


