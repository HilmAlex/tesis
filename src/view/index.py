from random import random
import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)

import json
import os
from view.build.IPRules import Ui_IPRules
from view.build.MACRules import Ui_MACRules
from view.build.main_window import Ui_MainWindow

cwd = os.getcwd()
ip_rules_path = f'{cwd}/src/data/initIPRules.json'
mac_rules_path = f'{cwd}/src/data/initMACRules.json'

def read(path):
    with open(path) as file:
        json_data = file.read()
        data = json.loads(json_data)
    
    return data

def write(path, new_data):
    with open(path, 'w') as out_file:
        json_data = json.dumps(new_data, indent=4)
        out_file.write(json_data)

def read_json(path):
    json_data = read(path)
    return json_data

def read_ip_rules():
    ip_rules = read_json(ip_rules_path)
    return ip_rules

def read_mac_rules():
    mac_rules = read_json(ip_rules_path)
    return mac_rules

def write_ip_rules(new_data):
    ip_rules = write(ip_rules_path,new_data)
    return ip_rules

def write_mac_rules(new_data):
    mac_rules = write(mac_rules_path,new_data)
    return mac_rules

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

        current_ip_rules = read_ip_rules()

        new_ip_rules = {
            "name": random.random(),
            "from": ip_from,
            "to": ip_to
        }

        current_ip_rules.add(new_ip_rules)

        write_ip_rules(current_ip_rules)
    
    def openMACDialog(self):
        IPRules = QDialog()
        ui = Ui_MACRules()
        ui.setupUi(IPRules)
        ui.accept_button.clicked.connect(lambda: self.handleMACDialogSubmit(ui))
        IPRules.exec()

    def handleMACDialogSubmit(self, ui):
        mac_from = ui.input_mac_from.text()
        mac_to= ui.input_mac_to.text()

        current_mac_rules = read_mac_rules()

        new_mac_rules = {
            "name": random(),
            "from": mac_from,
            "to": mac_to
        }

        current_mac_rules.add(new_mac_rules)

        write_mac_rules(current_mac_rules)


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
    

