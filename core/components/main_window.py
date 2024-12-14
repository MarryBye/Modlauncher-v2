from PySide6.QtCore import Qt, QPropertyAnimation, QRect
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QFontDatabase

from resources.ui.main_window_ui import Ui_MainWindow

from core.components.gallery_button import GalleryButton
from core.components.play_window import PlayWindow

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.connects()
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.animation = QPropertyAnimation(self.ui.navbar, b"geometry")
        
        self._is_moving = False
        self._start_pos = None
        self._window_minimized = False
        self._compact = True
        
        font_id = QFontDatabase.addApplicationFont("./resources/fonts/minecraft.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

        style = open("./resources/styles/main_window.qss").read() % font_family
        self.setStyleSheet(style)
        
    def connects(self):
        
        self.mousePressEvent = self.on_title_clicked
        self.mouseMoveEvent = self.on_title_move
        self.mouseReleaseEvent = self.on_title_release
        
        self.ui.close.clicked.connect(self.close)
        self.ui.minimize.clicked.connect(self.minimize_button)
        self.ui.hide.clicked.connect(self.showMinimized)
        self.ui.compact.clicked.connect(self.navbar_change_size)
        
        self.ui.maps.clicked.connect(self.open_maps)
        self.ui.modpacks.clicked.connect(self.open_modpacks)
        self.ui.play.clicked.connect(self.open_play_window)
    
    def on_title_clicked(self, event):
        if event.button() == Qt.LeftButton and self.ui.title.geometry().contains(event.pos()):
            self._is_moving = True
            self._start_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def on_title_move(self, event):
        if self._is_moving:
            self.move(event.globalPosition().toPoint() - self._start_pos)
            event.accept()

    def on_title_release(self, event):
        if event.button() == Qt.LeftButton:
            self._is_moving = False
            event.accept()
    
    def navbar_change_size(self, event):
        
        width = 200 if self._compact else 48
        self._compact = not self._compact
        
        startRect = self.ui.navbar.geometry()
        finalRect = QRect(startRect.left(), startRect.top(), width, startRect.height())
        
        self.animation.setDuration(125)
        self.animation.setStartValue(startRect)
        self.animation.setEndValue(finalRect)
        self.animation.valueChanged.connect(lambda rect: self.ui.navbar.setFixedWidth(rect.width()))
        
        self.animation.start()
        
    def minimize_button(self, event):
        if self._window_minimized:
            self.showMaximized()
        else:
            self.showNormal()
            
        self._window_minimized = not self._window_minimized
    
    def clear_main_layout(self):
        for i in reversed(range(self.ui.content_layout.count())):
            widget = self.ui.content_layout.itemAt(i).widget()  
            if widget is not None:
                self.ui.content_layout.removeWidget(widget) 
                widget.deleteLater() 
    
    def open_maps(self, event):
        self.clear_main_layout()
        
        row = 1
        for i in range(10):
            column = (i % 3) + 1
            
            new_btn = GalleryButton()
            new_btn.setFixedSize(self.width() / 3 - 16 * 6, 250)
            new_btn.set_image("./resources/images/gallery_button_test.jpg")
            
            
            self.ui.content_layout.addWidget(new_btn, row, column)
            
            if column == 3: row += 1
            
    def open_modpacks(self, event):
        self.clear_main_layout()
        
        row = 1
        for i in range(10):
            column = (i % 3) + 1
            
            new_btn = GalleryButton()
            new_btn.ui.name.setText("Сборка")
            new_btn.setFixedSize(self.width() / 3 - 16 * 6, 250)
            new_btn.set_image("./resources/images/gallery_button_test.jpg")
            
            self.ui.content_layout.addWidget(new_btn, row, column)
            
            if column == 3: row += 1
            
    def open_play_window(self, event):
        self.clear_main_layout()
        
        window = PlayWindow()
        self.ui.content_layout.addWidget(window, 1, 1)