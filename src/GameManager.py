"""Тут описываем изменения и влияния на статы"""
import time
import json

class GameManager:
    eatIndicator = None
    toiletIndicator = None
    moodIndicator = None

    delta = 0

    def __init__(self, pet):
        self.pet = pet


    def kill(self):
        self.pet.die()

    def changeParametrs(self):
        self.pet.eatIndicator -= 1
        self.pet.toiletIndicator -= 1
        self.pet.moodIndicator -= 1

    def mainThread(self):
        while True:
            if self.pet.eatIndicator < 0:
                self.kill()

            if self.delta == 10:
                self.delta = 0
                self.pet.saveParameters()
            else:
                time.sleep(10)
                self.changeParametrs()
                self.delta += 1
            self.pet.allWindows[2].changeParametrs(self.pet.eatIndicator,
                                                   self.pet.toiletIndicator,
                                                   self.pet.moodIndicator)
