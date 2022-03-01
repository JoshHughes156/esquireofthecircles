
class Item:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Weapon(Item):

    def __init__(self, name, weight, damage):
        super().__init__(name, weight)
        self.damage = damage

class Gear(Item):

    def __init__(self, name, weight, defense, place):
        super().__init__(name, weight)
        self.defense = defense
        self.place = place

