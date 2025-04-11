import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.toyota.toggled.connect(self.click)
        self.ui.peugeot.toggled.connect(self.click)
        self.ui.volvo.toggled.connect(self.click)
        self.show()

    def click(self):
        if self.ui.toyota.isChecked():
            self.ui.logo.setPixmap(QPixmap('./toyota.jpg'))
        elif self.ui.peugeot.isChecked():
            self.ui.logo.setPixmap(QPixmap('./peugeot.png'))
        elif self.ui.volvo.isChecked():
            self.ui.logo.setPixmap(QPixmap('./volvo.png'))

    def service(self):
        price = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())