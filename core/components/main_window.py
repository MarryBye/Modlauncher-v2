from PySide6.QtCore import Qt, QPropertyAnimation, QRect
from PySide6.QtWidgets import QMainWindow

from resources.ui.main_window_ui import Ui_MainWindow

from core.components.gallery_button import GalleryButton

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
        
    def connects(self):
        
        self.mousePressEvent = self.on_title_clicked
        self.mouseMoveEvent = self.on_title_move
        self.mouseReleaseEvent = self.on_title_release
        
        self.ui.close.clicked.connect(self.close)
        self.ui.minimize.clicked.connect(self.minimize_button)
        self.ui.hide.clicked.connect(self.showMinimized)
        self.ui.compact.clicked.connect(self.navbar_change_size)
        
        self.ui.maps.clicked.connect(self.open_maps)
    
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
        
    def open_maps(self, event):
        row = 1
        for i in range(10):
            column = (i % 3) + 1
            
            new_btn = GalleryButton()
            new_btn.setFixedSize(self.width() / 3 - 16 * 6, 250)
            new_btn.set_image("./resources/images/gallery_button_test.jpg")
            
            self.ui.content_layout.addWidget(new_btn, row, column)
            
            if column == 3: row += 1