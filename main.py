import sys

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from core.components.main_window import MainWindow

TITLE = "GMRS World Launcher"
VERSION = "Версия 1.0.0"
        
app = QApplication(sys.argv)

font_id = QFontDatabase.addApplicationFont("./resources/fonts/minecraft.ttf")
font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

style = open("./resources/styles/style.qss").read() % font_family
app.setStyleSheet(style)

win = MainWindow()

win.show()
app.exec()