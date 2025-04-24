import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.toyota.toggled.connect(self.click)
        self.ui.peugeot.toggled.connect(self.click)
        self.ui.volvo.toggled.connect(self.click)
        self.ui.reserve.clicked.connect(self.service)
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
        mileage = self.ui.kilometers.text()
        date = self.ui.date.text()

        if self.ui.service_check.isChecked():
            price += 200
        if self.ui.service_climate.isChecked():
            price += 150
        if self.ui.service_oil.isChecked():
            price += 300

        messeage = QMessageBox()
        messeage.setText(f"Podsumowanie: \n"
                         f"Cena: {price}, \n"
                         f"Przebieg: {mileage}, \n"
                         f"Data: {date} \n")
        messeage.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())