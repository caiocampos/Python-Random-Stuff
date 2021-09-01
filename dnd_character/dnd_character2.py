import random


def roll_dice():
    return random.randint(1, 6)


def modifier(constitution):
    return (constitution - 10) // 2


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        l = sorted(roll_dice() for _ in range(4))
        return sum(l[1:])
