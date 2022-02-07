from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui/test.ui', self)
        self.show()

        self.pushButton.clicked.connect(self.btn_callback)

    def btn_callback(self):
        print("qq")
        self.label.setText("qq")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()