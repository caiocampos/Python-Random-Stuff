EARTH = 31557600
MERCURY = EARTH * 0.2408467
VENUS = EARTH * 0.61519726
MARS = EARTH * 1.8808158
JUPITER = EARTH * 11.862615
SATURN = EARTH * 29.447498
URANUS = EARTH * 84.016846
NEPTUNE = EARTH * 164.79132


class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round(self.seconds / EARTH, 2)

    def on_mercury(self):
        return round(self.seconds / MERCURY, 2)

    def on_venus(self):
        return round(self.seconds / VENUS, 2)

    def on_mars(self):
        return round(self.seconds / MARS, 2)

    def on_jupiter(self):
        return round(self.seconds / JUPITER, 2)

    def on_saturn(self):
        return round(self.seconds / SATURN, 2)

    def on_uranus(self):
        return round(self.seconds / URANUS, 2)

    def on_neptune(self):
        return round(self.seconds / NEPTUNE, 2)
