import json

from PySide6 import QtGui, QtWidgets


"""
Класс описывающий нашего петомца 
    Его состояние и анимации их
    Взаимодействие с ним
"""

class Pet:
    lable = None
    allWindows = None

    pathParameters = "parameters.json"
    state = {"idle": "src/Animations/idle.gif",
             "grap": "src/Animations/grapIdle.gif",
             "pettingGood": "src/Animations/pettingGood.gif",
             "pettingBad": "src/Animations/pettingBad.gif",
             "eat": "src/Animations/eat.gif",
             "toilet": "src/Animations/toilet.gif",
             "game": "src/Animations/game.gif",
             "die": "src/Animations/die.gif"
             }

    cursor: {str: QtGui.Qt.CursorShape} = {"idle": QtGui.Qt.CursorShape.ArrowCursor,
                                           "grap": QtGui.Qt.CursorShape.OpenHandCursor,
                                           "pettingGood": QtGui.Qt.CursorShape.OpenHandCursor,
                                           "pettingBad": QtGui.Qt.CursorShape.OpenHandCursor,
                                           "eat": QtGui.Qt.CursorShape.ArrowCursor,
                                           "toilet": QtGui.Qt.CursorShape.ArrowCursor,
                                           "game": QtGui.Qt.CursorShape.ArrowCursor,
                                           "die": QtGui.Qt.CursorShape.ArrowCursor
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
        self.moodIndicator += 10
        if self.moodIndicator > 100:
            self.moodIndicator = 100
        self.currentState = "game"
        self.lable.changeMoveFinish(self.endAnimation)

    def eat(self):
        print("Кушать")
        self.eatIndicator += 30
        if self.eatIndicator > 100:
            self.eatIndicator = 100
        self.currentState = "eat"
        self.lable.changeMoveFinish(self.endAnimation)

    def toilet(self):
        print("Туалет")
        self.toiletIndicator = 100
        self.currentState = "toilet"
        self.lable.changeMoveFinish(self.endAnimation)

    def chatII(self):
        print("Чат")

    def timer(self):
        print("Таймер")
        #window = QtWidgets.QDialog()
        #app = src.UI.timerInit.Ui_Dialog(window)
        #window.exec()

    def parameters(self):
        print("Параметры")
        self.allWindows[1].show()
        self.allWindows[1].activateWindow()


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


    def setNewYear(self):
        print("Создаём новый год!")
        self.state = {"idle": "src/Animations/New_idle.gif",
                 "grap": "src/Animations/New_grapIdle.gif",
                 "pettingGood": "src/Animations/New_pettingGood.gif",
                 "pettingBad": "src/Animations/New_pettingBad.gif",
                 "eat": "src/Animations/eat.gif",
                 "toilet": "src/Animations/toilet.gif",
                 "game": "src/Animations/game.gif",
                 "die": "src/Animations/die.gif"
                 }


    def die(self):
        print("Тамагочи рип")
        self.currentState = "die"
        self.lable.changeMove()


    def endAnimation(self):
        self.currentState = "idle"
        self.lable.changeMove()
        print("Конец анимации")