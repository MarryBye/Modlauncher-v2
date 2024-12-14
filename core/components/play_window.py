from PySide6.QtCore import Qt, QPropertyAnimation, QRect
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QImage, QPixmap

from resources.ui.play_window_ui import Ui_play_window

class PlayWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.ui = Ui_play_window()
        self.ui.setupUi(self)
        
        style = open("./resources/styles/play_window.qss").read()
        self.setStyleSheet(style)