import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)

from view.build.IPRules import Ui_IPRules
from view.build.MACRules import Ui_MACRules

from .build.main_window import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.new_ip_rule = []
        self.new_mac_rule = []

    def openIPDialog(self):
        IPRules = QDialog()
        ui = Ui_IPRules()
        ui.setupUi(IPRules)
        ui.accept_button.clicked.connect(lambda: self.handleIPDialogSubmit(ui))
        IPRules.exec()

    def handleIPDialogSubmit(self, ui):
        ip_from = ui.input_ip_from.text()
        ip_to= ui.input_ip_to.text()

        print(ip_from, ip_to)
    
    def openMACDialog(self):
        IPRules = QDialog()
        ui = Ui_MACRules()
        ui.setupUi(IPRules)
        ui.accept_button.clicked.connect(lambda: self.handleMACDialogSubmit(ui))
        IPRules.exec()

    def handleMACDialogSubmit(self, ui):
        mac_from = ui.input_mac_from.text()
        mac_to= ui.input_mac_to.text()

        print(mac_from, mac_to)

    def connectSignalsSlots(self):
        self.open_ip_menu.triggered.connect(self.openIPDialog)
        self.open_mac_menu.triggered.connect(self.openMACDialog)
        self.actionA_cerca_de.triggered.connect(self.about)

    
    def print():
        print("Hola")

    def about(self):
        QMessageBox.about(
            self,
            "Acerca de Reglas Firewall",
            "<p>Una simple GUI construida con:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>"
            "<p>Creador:</p>"
            "<p>- Kevin Yepez</p>"
            "<p>Fecha de creacion:</p>"
            "<p>- **/**/**</p>",
        )
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
    

