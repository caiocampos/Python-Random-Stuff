import random


def roll_dice():
    return random.randint(1, 6)


def modifier(constitution):
    return (constitution - 10) // 2


class Character:
    def __init__(self):
        self.__strength = self.ability()
        self.__dexterity = self.ability()
        self.__constitution = self.ability()
        self.__intelligence = self.ability()
        self.__wisdom = self.ability()
        self.__charisma = self.ability()
        self.__hitpoints = 10 + modifier(self.__constitution)

    @property
    def strength(self):
        return self.__strength

    @property
    def dexterity(self):
        return self.__dexterity

    @property
    def constitution(self):
        return self.__constitution

    @property
    def intelligence(self):
        return self.__intelligence

    @property
    def wisdom(self):
        return self.__wisdom

    @property
    def charisma(self):
        return self.__charisma

    @property
    def hitpoints(self):
        return self.__hitpoints

    def ability(self):
        l = [roll_dice(), roll_dice(), roll_dice(), roll_dice()]
        l.remove(min(l))
        return sum(l)
