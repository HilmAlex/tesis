# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/view/source/reglas_IP.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IPRules(object):
    def setupUi(self, IPRules):
        IPRules.setObjectName("IPRules")
        IPRules.resize(431, 236)
        self.horizontalLayout = QtWidgets.QHBoxLayout(IPRules)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cancel_button = QtWidgets.QPushButton(IPRules)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(IPRules)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.input_ip_to = QtWidgets.QLineEdit(IPRules)
        self.input_ip_to.setObjectName("input_ip_to")
        self.gridLayout.addWidget(self.input_ip_to, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(IPRules)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.accept_button = QtWidgets.QPushButton(IPRules)
        self.accept_button.setObjectName("accept_button")
        self.gridLayout.addWidget(self.accept_button, 4, 2, 1, 1)
        self.input_ip_from = QtWidgets.QLineEdit(IPRules)
        self.input_ip_from.setObjectName("input_ip_from")
        self.gridLayout.addWidget(self.input_ip_from, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.label_2.setBuddy(self.input_ip_to)
        self.label.setBuddy(self.input_ip_from)

        self.retranslateUi(IPRules)
        self.cancel_button.clicked.connect(IPRules.reject)
        self.accept_button.clicked.connect(IPRules.accept)
        QtCore.QMetaObject.connectSlotsByName(IPRules)
        IPRules.setTabOrder(self.input_ip_from, self.input_ip_to)
        IPRules.setTabOrder(self.input_ip_to, self.cancel_button)
        IPRules.setTabOrder(self.cancel_button, self.accept_button)

    def retranslateUi(self, IPRules):
        _translate = QtCore.QCoreApplication.translate
        IPRules.setWindowTitle(_translate("IPRules", "Nueva regla IP"))
        self.cancel_button.setText(_translate("IPRules", "&Cancelar"))
        self.label_2.setText(_translate("IPRules", "IP &destino"))
        self.label.setText(_translate("IPRules", "IP &origen"))
        self.accept_button.setText(_translate("IPRules", "&Aplicar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IPRules = QtWidgets.QDialog()
    ui = Ui_IPRules()
    ui.setupUi(IPRules)
    IPRules.show()
    sys.exit(app.exec_())
