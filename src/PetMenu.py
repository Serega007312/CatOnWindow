from PySide6 import QtWidgets

class MenuPet(QtWidgets.QMenu):
    def __init__(self, pet):
        super().__init__()
        self.pet = pet
        self.addAction("Параметры", self.pet.parameters)
        self.addSeparator()
        self.addAction("Кормить", self.pet.eat)
        self.addAction("Играть", self.pet.game)
        self.addAction("В туалет", self.pet.toilet)
        self.addSeparator()
        self.addAction("Таймер", self.pet.timer)
        self.addAction("Чат", self.pet.chatII)
