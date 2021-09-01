import random
import string


class Robot(object):
    def __init__(self):
        self.__name = self.__random_name()

    def reset(self):
        self.__name = self.__random_name()

    def __random_name(self):
        random.seed()
        letters = string.ascii_uppercase
        number = random.randint(0, 999)
        a, b = random.choice(letters), random.choice(letters)
        return f"{a}{b}{number:03}"

    @property
    def name(self):
        return self.__name
