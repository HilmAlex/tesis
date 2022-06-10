# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/view/source/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1083, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1083, 22))
        self.menubar.setObjectName("menubar")
        self.menuNueva_regla = QtWidgets.QMenu(self.menubar)
        self.menuNueva_regla.setObjectName("menuNueva_regla")
        self.menuEliminar_regla = QtWidgets.QMenu(self.menubar)
        self.menuEliminar_regla.setObjectName("menuEliminar_regla")
        self.menu_Ayuda = QtWidgets.QMenu(self.menubar)
        self.menu_Ayuda.setObjectName("menu_Ayuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open_ip_menu = QtWidgets.QAction(MainWindow)
        self.open_ip_menu.setObjectName("open_ip_menu")
        self.open_mac_menu = QtWidgets.QAction(MainWindow)
        self.open_mac_menu.setObjectName("open_mac_menu")
        self.actionIP_2 = QtWidgets.QAction(MainWindow)
        self.actionIP_2.setObjectName("actionIP_2")
        self.actionMAC_2 = QtWidgets.QAction(MainWindow)
        self.actionMAC_2.setObjectName("actionMAC_2")
        self.actionA_cerca_de = QtWidgets.QAction(MainWindow)
        self.actionA_cerca_de.setObjectName("actionA_cerca_de")
        self.menuNueva_regla.addAction(self.open_ip_menu)
        self.menuNueva_regla.addAction(self.open_mac_menu)
        self.menuEliminar_regla.addAction(self.actionIP_2)
        self.menuEliminar_regla.addAction(self.actionMAC_2)
        self.menu_Ayuda.addAction(self.actionA_cerca_de)
        self.menubar.addAction(self.menuNueva_regla.menuAction())
        self.menubar.addAction(self.menuEliminar_regla.menuAction())
        self.menubar.addAction(self.menu_Ayuda.menuAction())

        self.retranslateUi(MainWindow)
        self.open_ip_menu.triggered.connect(self.open_ip_menu.hover)
        self.actionA_cerca_de.triggered.connect(self.actionA_cerca_de.hover)
        self.open_mac_menu.triggered.connect(self.open_mac_menu.hover)
        self.actionIP_2.destroyed.connect(self.open_ip_menu.deleteLater)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reglas Firewall"))
        self.label.setText(_translate("MainWindow", "COMIENCE A CREAR SUS NUEVAS REGLAS FIREWALL"))
        self.label_2.setText(_translate("MainWindow", "- Clic en Nueva regla para instalar reglas IP o MAC. Puede presionar ALT+N (atajo) para acceder a la lista desplegable de la opciòn."))
        self.label_3.setText(_translate("MainWindow", "- Clic en Eliminar regla para poder eliminar una regla ya instalada. Puede presionar ALT+E (atajo) para acceder a la lista desplegable de la opciòn."))
        self.label_7.setText(_translate("MainWindow", "- Configurar siempre IP/MAC de origen y destino antes de hacer clic en \"Aplicar\"."))
        self.label_6.setText(_translate("MainWindow", "- En las 2 opciones anteriores en susrepectivos cuadros de diàlogo puede desplazarse con el tabulador por las diferentes opciones."))
        self.label_4.setText(_translate("MainWindow", "- Clic en ayuda para ver informaciòn sobre la UI, fecha de creaciòn, creador, etc. Puede presionar ALT+A (atajo) para acceder a la lista desplegable de la opciòn."))
        self.label_5.setText(_translate("MainWindow", "NOTA: Configurar siempre igual reglas de IP y MAC. Por ejemplo, si configura 2 reglas IP debe configurar 2 reglas MAC o viceversa."))
        self.menuNueva_regla.setTitle(_translate("MainWindow", "&Nueva regla"))
        self.menuEliminar_regla.setTitle(_translate("MainWindow", "&Eliminar regla"))
        self.menu_Ayuda.setTitle(_translate("MainWindow", "&Ayuda"))
        self.open_ip_menu.setText(_translate("MainWindow", "IP"))
        self.open_ip_menu.setToolTip(_translate("MainWindow", "Nueva regla IP"))
        self.open_mac_menu.setText(_translate("MainWindow", "MAC"))
        self.open_mac_menu.setToolTip(_translate("MainWindow", "Nueva regla MAC"))
        self.actionIP_2.setText(_translate("MainWindow", "Eliminar IP"))
        self.actionIP_2.setToolTip(_translate("MainWindow", "Eliminar regla IP"))
        self.actionMAC_2.setText(_translate("MainWindow", "Eliminar MAC"))
        self.actionMAC_2.setToolTip(_translate("MainWindow", "Eliminar regla MAC"))
        self.actionA_cerca_de.setText(_translate("MainWindow", "A&bout.."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
