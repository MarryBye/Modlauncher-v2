from PySide6.QtCore import Qt, QPropertyAnimation, QRect
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QImage, QPixmap

from resources.ui.gallery_button_ui import Ui_gallery_button

class GalleryButton(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.ui = Ui_gallery_button()
        self.ui.setupUi(self)
        
        self.ui.buttons.setFixedHeight(0)
        
        self.animation = QPropertyAnimation(self.ui.buttons, b"geometry")
        
        self.enterEvent = self.show_buttons_section
        self.leaveEvent = self.hide_buttons_section
        
        style = open("./resources/styles/gallery_button.qss").read()
        self.setStyleSheet(style)
        
    def set_image(self, path):
        self._image = QPixmap(path)
        self.update_image()
    
    def update_image(self):
        scaled_image = self._image.scaled(
            self.ui.logo.width(),
            self.ui.logo.height()
        )
        self.ui.image.setPixmap(scaled_image)
        
    def resizeEvent(self, event):
        self.update_image()
        super().resizeEvent(event)
    
    def show_buttons_section(self, event):
        
        startRect = self.ui.buttons.geometry()
        finalRect = QRect(startRect.left(), startRect.top(), startRect.width(), 100)
        
        self.animation.setDuration(125)
        self.animation.setStartValue(startRect)
        self.animation.setEndValue(finalRect)
        self.animation.valueChanged.connect(lambda rect: self.ui.buttons.setFixedHeight(rect.height()))
        
        self.animation.start()
        
    def hide_buttons_section(self, event):
        startRect = self.ui.buttons.geometry()
        finalRect = QRect(startRect.left(), startRect.top(), startRect.width(), 0)
        
        self.animation.setDuration(125)
        self.animation.setStartValue(startRect)
        self.animation.setEndValue(finalRect)
        self.animation.valueChanged.connect(lambda rect: self.ui.buttons.setFixedHeight(rect.height()))
        
        self.animation.start()