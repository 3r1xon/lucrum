import sys, ctypes
import time


from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer


from Interface.IHome import IHome
from Interface.IError import IError


__author__ = "frday_"
__version__ = "31/03/2021 - frday_ & Moldark"


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def main():
    """***Launch the program***"""
    if is_admin():
        try:
            app = QApplication(sys.argv)

            splash = QSplashScreen(QPixmap('Resources\splash_screen.png'))

            splash.show()

            QTimer.singleShot(2000, lambda: splash.close())

            time.sleep(0.500)

            mainwindow = IHome(__version__)
            mainwindow.show()

            sys.exit(app.exec_())
        except Exception as e:
            error = IError(f"Fatal error, cannot run the app! {e}")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


if __name__ == "__main__":
    main()
