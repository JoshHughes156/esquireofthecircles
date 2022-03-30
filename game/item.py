
class Item:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Weapon(Item):

    def __init__(self, name, weight, damage, element=""):
        super().__init__(name, weight)
        self.damage = damage
        self.element = element

    matchups = {"fire":{"fire":1, "water":0.5, "air":1.5, "":1.2}, "water":{"fire":1.5, "water":1, "air":0.5, "":1.2}, "air":{"fire":0.5, "water":1.5, "air":1, "":1.2}, "":{"fire":0.8, "water":0.8, "air":0.8, "":1}}
    piece_contrib = {"helmet":0.2, "chestplate":0.5, "pants":0.2, "boots":0.1}
    piece_total_points = {"helmet":30, "chestplate":45, "pants":20, "boots":15}


    @staticmethod
    def damage_calc(self, weapon, armor, damage_scaling_factor=1.5):
        return weapon.damage # Remove this line to add element type matchups
        total = 0
        for piece in armor:
            if piece.element != "":
                total += weapon.damage * self.matchups[weapon.element][piece.element] * self.piece_contrib[piece.place] * (piece.defense/self.piece_total_points[piece.place])
        total *= damage_scaling_factor
        total = round(total)
        return total



class Gear(Item):

    def __init__(self, name, weight, defense, place, element="", setname=""):
        super().__init__(name, weight)
        self.defense = defense
        self.place = place
        self.setname = setname
        self.element = element

