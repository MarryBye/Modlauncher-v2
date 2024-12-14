# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(977, 657)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.window_layout = QVBoxLayout()
        self.window_layout.setSpacing(0)
        self.window_layout.setObjectName(u"window_layout")
        self.window_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.title = QFrame(self.centralwidget)
        self.title.setObjectName(u"title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setFrameShape(QFrame.Shape.StyledPanel)
        self.title.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.title)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_layout = QHBoxLayout()
        self.title_layout.setSpacing(0)
        self.title_layout.setObjectName(u"title_layout")
        self.window_name = QLabel(self.title)
        self.window_name.setObjectName(u"window_name")

        self.title_layout.addWidget(self.window_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.title_layout.addItem(self.horizontalSpacer)

        self.hide = QPushButton(self.title)
        self.hide.setObjectName(u"hide")
        self.hide.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.hide.setIcon(icon1)

        self.title_layout.addWidget(self.hide)

        self.minimize = QPushButton(self.title)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop))
        self.minimize.setIcon(icon2)

        self.title_layout.addWidget(self.minimize)

        self.close = QPushButton(self.title)
        self.close.setObjectName(u"close")
        self.close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.close.setIcon(icon3)

        self.title_layout.addWidget(self.close)


        self.horizontalLayout_2.addLayout(self.title_layout)


        self.window_layout.addWidget(self.title)

        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.main)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.main_layout = QHBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.navbar = QWidget(self.main)
        self.navbar.setObjectName(u"navbar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.navbar.sizePolicy().hasHeightForWidth())
        self.navbar.setSizePolicy(sizePolicy2)
        self.navbar.setMinimumSize(QSize(32, 0))
        self.navbar.setMaximumSize(QSize(175, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.navbar)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.navbar_layout = QVBoxLayout()
        self.navbar_layout.setSpacing(0)
        self.navbar_layout.setObjectName(u"navbar_layout")
        self.navbar_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.compact = QPushButton(self.navbar)
        self.compact.setObjectName(u"compact")
        self.compact.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditSelectAll))
        self.compact.setIcon(icon4)
        self.compact.setIconSize(QSize(32, 32))

        self.navbar_layout.addWidget(self.compact)

        self.play = QPushButton(self.navbar)
        self.play.setObjectName(u"play")
        self.play.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.play.setIcon(icon5)
        self.play.setIconSize(QSize(32, 32))

        self.navbar_layout.addWidget(self.play)

        self.modpacks = QPushButton(self.navbar)
        self.modpacks.setObjectName(u"modpacks")
        self.modpacks.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderNew))
        self.modpacks.setIcon(icon6)
        self.modpacks.setIconSize(QSize(32, 32))

        self.navbar_layout.addWidget(self.modpacks)

        self.maps = QPushButton(self.navbar)
        self.maps.setObjectName(u"maps")
        self.maps.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.maps.setIcon(icon7)
        self.maps.setIconSize(QSize(32, 32))

        self.navbar_layout.addWidget(self.maps)

        self.settings = QPushButton(self.navbar)
        self.settings.setObjectName(u"settings")
        self.settings.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        self.settings.setIcon(icon8)
        self.settings.setIconSize(QSize(32, 32))
        self.settings.setFlat(False)

        self.navbar_layout.addWidget(self.settings)

        self.forum = QPushButton(self.navbar)
        self.forum.setObjectName(u"forum")
        self.forum.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon9 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.NetworkWired))
        self.forum.setIcon(icon9)
        self.forum.setIconSize(QSize(32, 32))

        self.navbar_layout.addWidget(self.forum)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.navbar_layout.addItem(self.verticalSpacer)


        self.verticalLayout_6.addLayout(self.navbar_layout)


        self.main_layout.addWidget(self.navbar)

        self.content_scroll = QScrollArea(self.main)
        self.content_scroll.setObjectName(u"content_scroll")
        self.content_scroll.setWidgetResizable(True)
        self.content = QWidget()
        self.content.setObjectName(u"content")
        self.content.setGeometry(QRect(0, 0, 817, 595))
        self.gridLayout_2 = QGridLayout(self.content)
        self.gridLayout_2.setSpacing(16)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.content_layout = QGridLayout()
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setHorizontalSpacing(16)
        self.content_layout.setVerticalSpacing(8)

        self.gridLayout_2.addLayout(self.content_layout, 0, 0, 1, 1)

        self.content_scroll.setWidget(self.content)

        self.main_layout.addWidget(self.content_scroll)


        self.verticalLayout_4.addLayout(self.main_layout)


        self.window_layout.addWidget(self.main)

        self.info_panel = QFrame(self.centralwidget)
        self.info_panel.setObjectName(u"info_panel")
        self.info_panel.setFrameShape(QFrame.Shape.StyledPanel)
        self.info_panel.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.info_panel)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.info_panel_layout = QHBoxLayout()
        self.info_panel_layout.setSpacing(0)
        self.info_panel_layout.setObjectName(u"info_panel_layout")
        self.icon = QPushButton(self.info_panel)
        self.icon.setObjectName(u"icon")
        self.icon.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy3)
        icon10 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpenRecent))
        self.icon.setIcon(icon10)

        self.info_panel_layout.addWidget(self.icon)

        self.version_label = QLabel(self.info_panel)
        self.version_label.setObjectName(u"version_label")

        self.info_panel_layout.addWidget(self.version_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.info_panel_layout.addItem(self.horizontalSpacer_2)

        self.author = QPushButton(self.info_panel)
        self.author.setObjectName(u"author")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.author.sizePolicy().hasHeightForWidth())
        self.author.setSizePolicy(sizePolicy4)
        self.author.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon11 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.UserAvailable))
        self.author.setIcon(icon11)

        self.info_panel_layout.addWidget(self.author)


        self.horizontalLayout_4.addLayout(self.info_panel_layout)


        self.window_layout.addWidget(self.info_panel)


        self.verticalLayout_2.addLayout(self.window_layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.window_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.compact.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.play.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u0430\u0442\u044c", None))
        self.modpacks.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u043e\u0440\u043a\u0438", None))
        self.maps.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u0442\u044b", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.forum.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u0443\u043c GMRS World", None))
        self.version_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.author.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440", None))
    # retranslateUi

