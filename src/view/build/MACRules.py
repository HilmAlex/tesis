# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/view/source/reglas_MAC.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MACRules(object):
    def setupUi(self, MACRules):
        MACRules.setObjectName("MACRules")
        MACRules.resize(431, 236)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MACRules)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cancel_button = QtWidgets.QPushButton(MACRules)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(MACRules)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.input_mac_to = QtWidgets.QLineEdit(MACRules)
        self.input_mac_to.setObjectName("input_mac_to")
        self.gridLayout.addWidget(self.input_mac_to, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(MACRules)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.accept_button = QtWidgets.QPushButton(MACRules)
        self.accept_button.setObjectName("accept_button")
        self.gridLayout.addWidget(self.accept_button, 4, 2, 1, 1)
        self.input_mac_from = QtWidgets.QLineEdit(MACRules)
        self.input_mac_from.setObjectName("input_mac_from")
        self.gridLayout.addWidget(self.input_mac_from, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.label_2.setBuddy(self.input_mac_to)
        self.label.setBuddy(self.input_mac_from)

        self.retranslateUi(MACRules)
        self.cancel_button.clicked.connect(MACRules.reject)
        self.accept_button.clicked.connect(MACRules.accept)
        QtCore.QMetaObject.connectSlotsByName(MACRules)
        MACRules.setTabOrder(self.input_mac_from, self.input_mac_to)
        MACRules.setTabOrder(self.input_mac_to, self.cancel_button)
        MACRules.setTabOrder(self.cancel_button, self.accept_button)

    def retranslateUi(self, MACRules):
        _translate = QtCore.QCoreApplication.translate
        MACRules.setWindowTitle(_translate("MACRules", "Nueva regla MAC"))
        self.cancel_button.setText(_translate("MACRules", "&Cancelar"))
        self.label_2.setText(_translate("MACRules", "MAC &destino"))
        self.label.setText(_translate("MACRules", "MAC &origen"))
        self.accept_button.setText(_translate("MACRules", "&Aplicar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MACRules = QtWidgets.QDialog()
    ui = Ui_MACRules()
    ui.setupUi(MACRules)
    MACRules.show()
    sys.exit(app.exec_())
