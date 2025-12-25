from PySide6 import QtWidgets, QtCore, QtGui


from src.PetMenu import MenuPet

class Label (QtWidgets.QLabel):
    def __init__(self, window, pet):
        super().__init__()
        self.petting = False
        self.oldPos = None
        self.windows = window
        self.pet = pet
        self.menu = MenuPet(pet=pet)


    def enterEvent(self, event, /):
        self.petting = True


    def wheelEvent(self, event, /):
        if self.petting != False:
            if event.angleDelta().y() < 0:
                self.pet.currentState = "pettingGood"
                self.setCursor(self.pet.cursor["pettingGood"])
                self.changeMove()
                self.movie().setCacheMode(QtGui.QMovie.CacheMode.CacheAll)
                self.movie().finished.connect(self.finishAnimation)
                self.petting = False

            else:
                self.pet.currentState = "pettingBad"
                self.setCursor(self.pet.cursor["pettingBad"])
                self.changeMove()
                self.movie().setCacheMode(QtGui.QMovie.CacheMode.CacheAll)
                self.movie().finished.connect(self.finishAnimation)
                self.petting = False


    def mousePressEvent(self, ev, /) -> None:
        if QtCore.Qt.MouseButton.LeftButton == ev.button():
            self.oldPos = ev.globalPos()
            self.pet.currentState = "grap"
            self.setCursor(self.pet.cursor["grap"])
            self.changeMove()

        if QtCore.Qt.MouseButton.RightButton == ev.button():
            self.menu.popup(ev.globalPos())

    def mouseMoveEvent(self, ev, /) -> None:
        if self.oldPos != None:
            delta = ev.globalPos() - self.oldPos
            self.parent().move(self.parent().pos() + delta)
            self.oldPos = ev.globalPos()

    def mouseReleaseEvent(self, ev, /) -> None:
        self.oldPos = None
        self.pet.currentState = "idle"
        self.setCursor(self.pet.cursor["idle"])
        self.changeMove()

    def leaveEvent(self, event, /):
        self.petting = False
        #self.pet.currentState = "idle"
        #self.setCursor(self.pet.cursor["idle"])
        #self.changeMove()

    def changeMove(self):
        self.movie().stop()
        self.setMovie(QtGui.QMovie(f"{self.pet.state[self.pet.currentState]}"))
        self.movie().start()

    def changeMoveFinish(self, func):
        self.movie().stop()
        self.setMovie(QtGui.QMovie(f"{self.pet.state[self.pet.currentState]}"))
        self.movie().start()
        self.movie().setCacheMode(QtGui.QMovie.CacheMode.CacheAll)
        self.movie().finished.connect(func)

    def finishAnimation(self):
        self.petting = True
        print("Конец")

