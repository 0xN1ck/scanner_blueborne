# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CVE-2017-0781_gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_CVE3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 160)
        MainWindow.setMinimumSize(QtCore.QSize(843, 160))
        MainWindow.setMaximumSize(QtCore.QSize(843, 160))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 821, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("font: 75 28pt \"Cantarell\";\n"
"text-decoration: underline;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_2.setMaximumSize(QtCore.QSize(250, 35))
        self.label_2.setStyleSheet("font: 75 14pt \"Open Sans Condensed\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.text_mac_3 = QtWidgets.QTextEdit(self.layoutWidget)
        self.text_mac_3.setMinimumSize(QtCore.QSize(200, 0))
        self.text_mac_3.setMaximumSize(QtCore.QSize(300, 35))
        self.text_mac_3.setObjectName("text_mac_3")
        self.horizontalLayout.addWidget(self.text_mac_3)
        self.attack_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.attack_3.setMinimumSize(QtCore.QSize(150, 45))
        self.attack_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.attack_3.setObjectName("attack_3")
        self.horizontalLayout.addWidget(self.attack_3)
        self.button_exit_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.button_exit_3.setMinimumSize(QtCore.QSize(150, 45))
        self.button_exit_3.setObjectName("button_exit_3")
        self.horizontalLayout.addWidget(self.button_exit_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CVE-2017-1000250"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">CVE-2017-0781</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Введите mac-адрес"))
        self.attack_3.setText(_translate("MainWindow", "Атака"))
        self.button_exit_3.setText(_translate("MainWindow", "Выход"))


