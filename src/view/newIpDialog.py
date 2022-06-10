from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)

from build.IPRules import Ui_IPRules

class IpDialog(QDialog, Ui_IPRules):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    