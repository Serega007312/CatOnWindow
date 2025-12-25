import sys
import threading

from PySide6 import QtWidgets, QtCore, QtGui

import src.GameManager
from src.Pet import Pet
from src.Label import Label
from src.UI.parametrs import Ui_MainWindow

class MainWindows(QtWidgets.QMainWindow):
    label = None
    pet = None
    def __init__(self):
        super().__init__()

    def initUi(self):
        self.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint | QtCore.Qt.WindowType.FramelessWindowHint)   #Убирает верхний хотбар
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)                                       #Делаем прозрачный фон
        self.resize(200, 200)

        self.movie = QtGui.QMovie("src/Animations/idle.gif")

        self.label.setMovie(self.movie)

        self.movie.start()
        self.setCentralWidget(self.label)

class Window2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindows()
    pet = Pet()  # Создаём питомца
    label = Label(window, pet)  # Создаем виджет для GIF
    pet.lable = label
    window.label = label
    window.pet = pet
    window.initUi()


    # Creat all windows...
    window2 = Window2()
    parametrsWindow = Ui_MainWindow()
    parametrsWindow.setupUi(window2)

    # Pet -> allWindows
    pet.allWindows = []
    pet.allWindows.append(window)
    pet.allWindows.append(window2)
    pet.allWindows.append(parametrsWindow)

    # Menu Tray
    menuTrey = QtWidgets.QMenu()
    menuTrey.addAction("Выход", app.exit)


    # Threading
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