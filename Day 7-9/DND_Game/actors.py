import random

class Creature:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def defensive_roll(self):
        roll = random.randint(1, 12)
        return roll * self.level

class Dragon(Creature):

    def __init__(self, name, level, scaliness, breathesfire):
        super.__init__(name, level)
        self.breathesfire = breathesfire
        self.scaliness = scaliness

    def defensive_roll(self):
        roll = random.randint(1, 12)
        return roll * self.level * self.scaliness
        if self.breathesfire:
            value = value * 2
        return value

class Wizard(Creature):

    def attack(self, creature):
        my_roll = self.defensive_roll()
        their_roll = self.defensive_roll()

