# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gallery_button.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_gallery_button(object):
    def setupUi(self, gallery_button):
        if not gallery_button.objectName():
            gallery_button.setObjectName(u"gallery_button")
        gallery_button.resize(364, 452)
        self.verticalLayout_2 = QVBoxLayout(gallery_button)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gallery_button_layout = QVBoxLayout()
        self.gallery_button_layout.setSpacing(0)
        self.gallery_button_layout.setObjectName(u"gallery_button_layout")
        self.logo = QWidget(gallery_button)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.logo)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.image = QLabel(self.logo)
        self.image.setObjectName(u"image")
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        self.image.setFont(font)
        self.image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.image)

        self.name = QLabel(self.logo)
        self.name.setObjectName(u"name")
        self.name.setFont(font)
        self.name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.name)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.gallery_button_layout.addWidget(self.logo)

        self.buttons = QWidget(gallery_button)
        self.buttons.setObjectName(u"buttons")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.buttons)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.download = QPushButton(self.buttons)
        self.download.setObjectName(u"download")
        self.download.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.download)

        self.description = QPushButton(self.buttons)
        self.description.setObjectName(u"description")
        self.description.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.description)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.gallery_button_layout.addWidget(self.buttons)


        self.verticalLayout_2.addLayout(self.gallery_button_layout)


        self.retranslateUi(gallery_button)

        QMetaObject.connectSlotsByName(gallery_button)
    # setupUi

    def retranslateUi(self, gallery_button):
        gallery_button.setWindowTitle(QCoreApplication.translate("gallery_button", u"Form", None))
        self.image.setText(QCoreApplication.translate("gallery_button", u"TextLabel", None))
        self.name.setText(QCoreApplication.translate("gallery_button", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.download.setText(QCoreApplication.translate("gallery_button", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c", None))
        self.description.setText(QCoreApplication.translate("gallery_button", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
    # retranslateUi

