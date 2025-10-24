import json

from PySide6 import QtGui, QtWidgets

import src.UI.dialog

"""
Класс описывающий нашего петомца 
    Его состояние и анимации их
    Взаимодействие с ним
"""

class Pet:
    pathParameters = "parameters.json"
    state = {"idle": "src/Animations/idle.gif",
             "grap": "src/Animations/grapIdle.gif",
             "pettingGood": "src/Animations/pettingGood.gif",
             "pettingBad": "src/Animations/pettingBad.gif"
             }
    cursor: {str: QtGui.Qt.CursorShape} = {"idle": QtGui.Qt.CursorShape.ArrowCursor,
                                           "grap": QtGui.Qt.CursorShape.OpenHandCursor,
                                           "pettingGood": QtGui.Qt.CursorShape.OpenHandCursor,
                                           "pettingBad": QtGui.Qt.CursorShape.OpenHandCursor,
                                           }


    # Основные параметры
    eatIndicator = 100
    toiletIndicator = 100
    moodIndicator = 100

    def __init__(self):
        self.currentState = "idle"
        self.readParameters()


    def game(self):
        print("Игра")

    def eat(self):
        print("Кушать")

    def toilet(self):
        print("Туалет")

    def chatII(self):
        print("Чат")

    def timer(self):
        print("Таймер")
        #window = QtWidgets.QDialog()
        #app = src.UI.timerInit.Ui_Dialog(window)
        #window.exec()

    def parameters(self):
        print("Параметры")
        window = QtWidgets.QDialog()
        app = src.UI.dialog.Ui_Dialog(window, self.eatIndicator,self.toiletIndicator,self.moodIndicator)
        window.exec()


    def saveParameters(self):
        with open(self.pathParameters, "w") as file:
            data = {
                "eatIndicator": self.eatIndicator,
                "toiletIndicator": self.toiletIndicator,
                "moodIndicator": self.moodIndicator
            }
            json_string = json.dumps(data)
            file.write(json_string)
        print("Сохраняю параметры")

    def readParameters(self):
        with open(self.pathParameters, "r") as file:
            data = json.load(file)
            self.eatIndicator = data["eatIndicator"]
            self.toiletIndicator = data["toiletIndicator"]
            self.moodIndicator = data["moodIndicator"]
        print("Данные прочитаны")


    def die(self):
        print("Тамагочи рип")