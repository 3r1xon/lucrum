import platform
import json

"""*** Imports from the PyQt5 stuff ***"""
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore


"""*** Imports all the scripts to run ***"""
from Scripts.booster import Boost
from Scripts.downloader import Downloader

from Interface.IError import IError
from Interface.IYesNo import IYesNo
from Interface.IActivator import IActivator


class IHome(QMainWindow):
    def __init__(self, version):
        super().__init__()
        loadUi('UI\main_window.ui', self)
        """***
            The "first widget" is the left side menu
            and the "second widget" is the right side
            menu
        ***"""
        self.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.FramelessWindowHint
        )
        self.BTN_Close.clicked.connect(lambda: self.close())
        self.BTN_Hide.clicked.connect(lambda: self.showMinimized())

        """--- ADMIN MODE ---"""
        self.BTN_Admin_Mode.clicked.connect(lambda: IActivator())


        self.LINE_Version.setPlaceholderText(f"Version: {version}")

        """--- Platform info ---"""
        self.Platform_Win.setPlaceholderText(f"Windows: {platform.version()}")
        self.Platform_CPU.setPlaceholderText(f"CPU: {platform.processor()} ")
        self.Platform_Architecture.setPlaceholderText(f"{platform.architecture()}")



        """*** Boost page of the widget ***"""
        self.BTN_Boost.clicked.connect(lambda: self.stackedWidget_MENU.setCurrentWidget(self.PAGE_Boost))
        self.BTN_Boost.clicked.connect(lambda: self.stackedWidget_BIG.setCurrentWidget(self.PAGE_Lucrum_Boost))


        """*** Lucrum page of the second widget  ***"""
        self.BTN_Lucrum_Boost.clicked.connect(lambda: IYesNo(lambda: Boost()))
        self.BTN_Clean.clicked.connect(lambda: Boost.clean(self))


        """*** Utilities page of the widget ***"""
        self.BTN_Utilities.clicked.connect(lambda: self.stackedWidget_MENU.setCurrentWidget(self.PAGE_Utilities))
        self.BTN_Utilities.clicked.connect(lambda: self.stackedWidget_BIG.setCurrentWidget(self.PAGE_Installer))
        self.BTN_Utilities.clicked.connect(lambda: self.load_data("installations"))

        """*** Installer page of the second widget ***"""
        self.BTN_Installer.clicked.connect(lambda: self.stackedWidget_BIG.setCurrentWidget(self.PAGE_Installer))
        self.BTN_Add.clicked.connect(lambda: self.add_to_json(self.LINE_Name.text(), self.LINE_Link.text()))
        self.BTN_Add.clicked.connect(lambda: self.load_data("installations"))
        self.BTN_Remove.clicked.connect(lambda: self.remove_from_json())
        self.BTN_Remove.clicked.connect(lambda: self.load_data("installations"))
        self.BTN_Clear_Text.clicked.connect(lambda: self.clear_line())
        self.TBL_Installations.setColumnWidth(0, 300) # 170
        self.TBL_Installations.setColumnWidth(1, 200) # 183
        self.BTN_Install.clicked.connect(lambda: Downloader(self.data["installations"][self.TBL_Installations.currentRow()]["url"], self.data["installations"][self.TBL_Installations.currentRow()]["name"]))
        self.BTN_Install.clicked.connect(lambda: self.LBL_Loading.setText(f"Downloading: {self.data['installations'][self.TBL_Installations.currentRow()]['name']}"))
        self.BTN_Up.clicked.connect(lambda: self.sort('up'))
        self.BTN_Down.clicked.connect(lambda: self.sort('down'))

        with open('Data/custom-installs.json') as file:
            try:
                self.data = json.load(file)
            except Exception as e:
                error = IError(f"The JSON file failed to load! {e}")
                error.exec_()
        #self.TBL_Installations.cellDoubleClicked.connect(self.TBL_db_CLICKEVENT)


        """*** Downloader page of the second widget ***"""
        self.BTN_Downloader.clicked.connect(lambda: self.stackedWidget_BIG.setCurrentWidget(self.PAGE_Downloader))
        self.BTN_Mp3.clicked.connect(lambda: Downloader.download_from_yt(self, self.LINE_URL.text(), self.CMB_Quality.currentText(), mode='mp3'))
        self.BTN_Mp4.clicked.connect(lambda: Downloader.download_from_yt(self, self.LINE_URL.text(), self.CMB_Quality.currentText(), mode='mp4'))
        self.BTN_Clear_Text_2.clicked.connect(lambda: self.clear_line())


        """*** Options page of the widget ***"""
        self.BTN_Options.clicked.connect(lambda: self.stackedWidget_MENU.setCurrentWidget(self.PAGE_Options))
        self.BTN_Options.clicked.connect(lambda : self.stackedWidget_BIG.setCurrentWidget(self.PAGE_Settings))

        """*** Info page of the widget ***"""
        self.BTN_Info.clicked.connect(lambda: self.stackedWidget_BIG.setCurrentWidget(self.PAGE_Info))

        """*** Manager page of the second widget ***"""
        self.TBL_Manager.setColumnWidth(0, 300) # 170
        self.TBL_Manager.setColumnWidth(1, 200) # 183
        self.BTN_Local_Manager.clicked.connect(lambda: self.load_data("passwords"))
        self.BTN_Local_Manager.clicked.connect(lambda: self.stackedWidget_BIG.setCurrentWidget(self.PAGE_Local_Manager))
        self.BTN_Add_2.clicked.connect(lambda: self.add_to_json(self.LINE_Website_Name.text(), self.LINE_Password.text(), mode="manager"))
        self.BTN_Add_2.clicked.connect(lambda: self.load_data("passwords"))
        self.BTN_Remove_2.clicked.connect(lambda: self.remove_from_json("passwords"))
        self.BTN_Remove_2.clicked.connect(lambda: self.load_data("passwords"))
        self.BTN_Clear_Text_3.clicked.connect(lambda: self.clear_line())
        self.BTN_Up_2.clicked.connect(lambda: self.sort("up", "passwords", "password"))
        self.BTN_Down_2.clicked.connect(lambda: self.sort("down", "passwords", "password"))
        self.BTN_Info.clicked.connect(lambda: self.stackedWidget_MENU.setCurrentWidget(self.PAGE_Options))

    def add_to_json(self, name, url_password, mode=""):
        if mode == "":
            name = f"{name.replace(' ', '_')}.exe"
            self.data["installations"].append({"name": name, "url": url_password})
        else:
            if name == "" or url_password == "":
                return None

            a = 0
            for i in self.data["passwords"]:
                if name == self.data["passwords"][a]["name"] and url_password == self.data["passwords"][a]["password"]:
                    error = IError("Name and password already in list!")
                    error.exec_()
                    return None
                a += 1
            a = 0

            self.data["passwords"].append({"name" : name, "password": url_password})

        with open('Data/custom-installs.json', 'w') as f:
            json.dump(self.data, f, indent=4)

        self.clear_line()

        return None


    def remove_from_json(self, mode=""):
        if mode == "":
            del self.data["installations"][self.TBL_Installations.currentRow()]
        else:
            del self.data["passwords"][self.TBL_Manager.currentRow()]

        with open('Data/custom-installs.json', 'w') as f:
            json.dump(self.data, f, indent=4)


    def load_data(self, data_type):
        with open('Data/custom-installs.json') as file:
            try:
                data = json.load(file)
            except:
                error = IError("The JSON file failed to load!")
                error.exec_()
                return None

        tablerow = 0

        if data_type == "installations":
            self.TBL_Installations.setRowCount(len(data["installations"]))
            self.TBL_Installations.setColumnCount(2)
        else:
            self.TBL_Manager.setRowCount(len(data[data_type]))
            self.TBL_Manager.setColumnCount(2)

        for row in data[data_type]:
            self.TBL_Installations.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row["name"]))
            self.TBL_Manager.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row["name"]))
            tablerow += 1

        tablerow = 0
        if data_type == "installations":
            for row in data["installations"]:
                self.TBL_Installations.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row["url"]))
                tablerow += 1
        else:
            for row in data[data_type]:
                self.TBL_Manager.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row["password"]))
                tablerow += 1

    def sort(self, mode, arr="installations", set="url"):
        # Questo codice è da rivedere, anche se funziona non è ottimizzato al meglio
        # l'ho fatto mentre ero mezzo addormentato
        if arr == "installations":
            row = self.TBL_Installations.currentRow()
        else:
            row = self.TBL_Manager.currentRow()
        if mode == 'up':
            if row-1 < 0:
                return None

            remember_url = self.data[arr][row-1][set]
            remember_name = self.data[arr][row-1]["name"]

            self.data[arr][row-1][set] = self.data[arr][row][set]
            self.data[arr][row-1]["name"] = self.data[arr][row]["name"]

            self.data[arr][row]["name"] = remember_name
            self.data[arr][row][set] = remember_url

            with open('Data/custom-installs.json', 'w') as f:
                json.dump(self.data, f, indent=4)

            self.load_data(arr)
            row -= 1
            if arr == "installations":
                self.TBL_Installations.selectRow(row)
            else:
                self.TBL_Manager.selectRow(row)
        else:
            if row+1 > len(self.data[arr])-1:
                return None

            remember_url = self.data[arr][row+1][set]
            remember_name = self.data[arr][row+1]["name"]

            self.data[arr][row+1][set] = self.data[arr][row][set]
            self.data[arr][row+1]["name"] = self.data[arr][row]["name"]

            self.data[arr][row]["name"] = remember_name
            self.data[arr][row][set] = remember_url

            with open('Data/custom-installs.json', 'w') as f:
                json.dump(self.data, f, indent=4)

            self.load_data(arr)
            row += 1
            if arr == "installations":
                self.TBL_Installations.selectRow(row)
            else:
                self.TBL_Manager.selectRow(row)



    def clear_line(self):
        clearize = [self.LINE_Link, self.LINE_Name, self.LINE_URL, self.LINE_Website_Name, self.LINE_Password]
        for _ in clearize:
            _.clear()



    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)
