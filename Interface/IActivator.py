import sys
import os
import subprocess
import threading

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class IActivator(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('UI\crack.ui', self)
        self.BTN_Home.clicked.connect(lambda: self.crack_windows(mode='Home'))
        self.BTN_Pro.clicked.connect(lambda: self.crack_windows(mode='Pro'))
        self.BTN_Pro_N.clicked.connect(lambda: self.crack_windows(mode='Pro_N'))
        self.exec_()



    def crack_windows(self, mode):
        def start_thread():
            if mode == 'Home':
                commandlist = ["""slmgr.vbs /upk""",
                """slmgr.vbs /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99""",
                """slmgr.vbs /skms kms.lotro.cc""",
                """slmgr.vbs /ato"""]

                for _ in commandlist:
                    os.system(_)

            elif mode == 'Pro':
                commandlist = ["""slmgr.vbs /upk""",
                """slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX""",
                """slmgr.vbs /skms kms.lotro.cc""",
                """slmgr.vbs /ato"""]

                for _ in commandlist:
                    os.system(_)

            else:
                commandlist = ["""slmgr.vbs /upk""",
                """slmgr.vbs /ipk WGGHN-J84D6-QYCPR-T7PJ7-X766F""",
                """slmgr.vbs /skms kms.lotro.cc""",
                """slmgr.vbs /ato"""]

                for _ in commandlist:
                    os.system(_)

        t = threading.Thread(target=start_thread, args=())
        return t.start()
