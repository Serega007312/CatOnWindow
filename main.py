import sys
import threading

from PySide6 import QtWidgets, QtCore, QtGui

import src.GameManager
from src.Pet import Pet
from src.Label import Label


class MainWindows(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.pet = Pet()                        #Создаём питомца
        self.label = Label(self, self.pet)      #Создаем виджет для GIF
        self.initUi()

    def initUi(self):
        self.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint | QtCore.Qt.WindowType.FramelessWindowHint)   #Убирает верхний хотбар
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)                                       #Делаем прозрачный фон


        self.label.grabMouse()
        self.movie = QtGui.QMovie("src/Animations/idle.gif")

        self.label.setMovie(self.movie)

        self.movie.start()
        self.setCentralWidget(self.label)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindows()

    # Menu Tray
    menuTrey = QtWidgets.QMenu()
    menuTrey.addAction("Выход", app.exit)


    # threading
    mainThread = src.GameManager.GameManager(pet=window.pet)
    newThread = threading.Thread(target=mainThread.mainThread, daemon=True)
    newThread.start()

    # Tray
    icon = QtGui.QIcon("src/icon/icon.ico")
    tray = QtWidgets.QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)
    tray.setContextMenu(menuTrey)

    # Open main Window
    window.show()

    sys.exit(app.exec())