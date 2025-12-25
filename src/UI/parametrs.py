from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QProgressBar,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    eat = 0
    toilet = 0
    mood = 0

    def changeParametrs(self, eat_, toilet_, mood_):
        self.progressEat.setValue(eat_)
        self.progressToilet.setValue(toilet_)
        self.progressMood.setValue(mood_)
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(570, 374)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 541, 319))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.eatIndicator = QLabel(self.widget)
        self.eatIndicator.setObjectName(u"eatIndicator")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.eatIndicator.setFont(font1)
        self.eatIndicator.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.eatIndicator.setMargin(10)

        self.verticalLayout.addWidget(self.eatIndicator)

        self.progressEat = QProgressBar(self.widget)
        self.progressEat.setObjectName(u"progresEat")
        self.progressEat.setFont(font1)
        self.progressEat.setValue(24)

        self.verticalLayout.addWidget(self.progressEat)

        self.moodIndicator = QLabel(self.widget)
        self.moodIndicator.setObjectName(u"moodIndicator")
        self.moodIndicator.setFont(font1)
        self.moodIndicator.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.moodIndicator.setMargin(10)

        self.verticalLayout.addWidget(self.moodIndicator)

        self.progressMood = QProgressBar(self.widget)
        self.progressMood.setObjectName(u"progressMood")
        self.progressMood.setFont(font1)
        self.progressMood.setValue(24)

        self.verticalLayout.addWidget(self.progressMood)

        self.toiletIndicator = QLabel(self.widget)
        self.toiletIndicator.setObjectName(u"toiletIndicator")
        self.toiletIndicator.setFont(font1)
        self.toiletIndicator.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.toiletIndicator.setMargin(10)

        self.verticalLayout.addWidget(self.toiletIndicator)

        self.progressToilet = QProgressBar(self.widget)
        self.progressToilet.setObjectName(u"progressToilet")
        self.progressToilet.setFont(font1)
        self.progressToilet.setValue(24)

        self.verticalLayout.addWidget(self.progressToilet)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)



        #------------------------------------------------------




        #------------------------------------------------------

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.eatIndicator.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0434\u0430", None))
        self.moodIndicator.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435", None))
        self.toiletIndicator.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0430\u043b\u0435\u0442", None))
    # retranslateUi

