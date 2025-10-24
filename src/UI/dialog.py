# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QProgressBar,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    eat = 0
    toilet = 0
    mood = 0

    def __init__(self,dialog,eat_,toilet_,mood_):
        self.setupUi(dialog)
        self.progressEat.setValue(eat_)
        self.progressToilet.setValue(toilet_)
        self.progressMood.setValue(mood_)


    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 340)
        self.MainLable = QLabel(Dialog)
        self.MainLable.setObjectName(u"MainLable")
        self.MainLable.setGeometry(QRect(10, 0, 381, 41))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        self.MainLable.setFont(font)
        self.MainLable.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MainLable.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 50, 381, 242))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.widget.setFont(font1)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.eatIndicator = QLabel(self.widget)
        self.eatIndicator.setObjectName(u"eatIndicator")
        self.eatIndicator.setFont(font1)
        self.eatIndicator.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.eatIndicator.setMargin(10)

        self.verticalLayout.addWidget(self.eatIndicator)

        self.progressEat = QProgressBar(self.widget)
        self.progressEat.setObjectName(u"progresEat")
        self.progressEat.setFont(font1)
        self.progressEat.setOrientation(Qt.Orientation.Horizontal)
        self.progressEat.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.progressEat)

        self.moodIndicator = QLabel(self.widget)
        self.moodIndicator.setObjectName(u"moodIndicator")
        self.moodIndicator.setFont(font1)
        self.moodIndicator.setMargin(10)

        self.verticalLayout.addWidget(self.moodIndicator)

        self.progressMood = QProgressBar(self.widget)
        self.progressMood.setObjectName(u"progressMood")
        self.progressMood.setFont(font1)


        self.verticalLayout.addWidget(self.progressMood)

        self.toiletIndicator = QLabel(self.widget)
        self.toiletIndicator.setObjectName(u"toiletIndicator")
        self.toiletIndicator.setFont(font1)
        self.toiletIndicator.setMargin(10)

        self.verticalLayout.addWidget(self.toiletIndicator)

        self.progressToilet = QProgressBar(self.widget)
        self.progressToilet.setObjectName(u"progressToilet")
        self.progressToilet.setFont(font1)

        self.verticalLayout.addWidget(self.progressToilet)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.MainLable.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.eatIndicator.setText(QCoreApplication.translate("Dialog", u"\u0415\u0434\u0430", None))
        self.moodIndicator.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435", None))
        self.toiletIndicator.setText(QCoreApplication.translate("Dialog", u"\u0422\u0443\u0430\u043b\u0435\u0442", None))
    # retranslateUi

