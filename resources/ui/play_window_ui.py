# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'play_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_play_window(object):
    def setupUi(self, play_window):
        if not play_window.objectName():
            play_window.setObjectName(u"play_window")
        play_window.resize(756, 505)
        self.verticalLayout = QVBoxLayout(play_window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.news_box = QTextEdit(play_window)
        self.news_box.setObjectName(u"news_box")
        self.news_box.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.news_box.sizePolicy().hasHeightForWidth())
        self.news_box.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        self.news_box.setFont(font)

        self.main_layout.addWidget(self.news_box)

        self.bottom_panel = QWidget(play_window)
        self.bottom_panel.setObjectName(u"bottom_panel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bottom_panel.sizePolicy().hasHeightForWidth())
        self.bottom_panel.setSizePolicy(sizePolicy1)
        self.bottom_panel.setMinimumSize(QSize(0, 48))
        self.horizontalLayout_3 = QHBoxLayout(self.bottom_panel)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.version = QComboBox(self.bottom_panel)
        self.version.setObjectName(u"version")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.version.sizePolicy().hasHeightForWidth())
        self.version.setSizePolicy(sizePolicy2)
        self.version.setFont(font)
        self.version.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.version.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.version)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.start_game = QPushButton(self.bottom_panel)
        self.start_game.setObjectName(u"start_game")
        sizePolicy2.setHeightForWidth(self.start_game.sizePolicy().hasHeightForWidth())
        self.start_game.setSizePolicy(sizePolicy2)
        self.start_game.setFont(font)
        self.start_game.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.start_game.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.start_game)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.main_layout.addWidget(self.bottom_panel)


        self.verticalLayout.addLayout(self.main_layout)


        self.retranslateUi(play_window)

        QMetaObject.connectSlotsByName(play_window)
    # setupUi

    def retranslateUi(self, play_window):
        play_window.setWindowTitle(QCoreApplication.translate("play_window", u"Form", None))
        self.version.setPlaceholderText(QCoreApplication.translate("play_window", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0432\u0435\u0440\u0441\u0438\u044e...", None))
        self.start_game.setText(QCoreApplication.translate("play_window", u"\u0418\u0433\u0440\u0430\u0442\u044c", None))
    # retranslateUi

