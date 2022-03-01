
class Entity:
    
    def __init__(self, name. health, location, inventory=list(), armor=list(), money=0, inv_max_weight=0):
        self.name = name
        self.health = health
        self.location = location
        self.inventory = inventory
        self.armor = armor
        self.money = money
        self.inv_max_weight = inv_max_weight

    def take_damage(self, damage):
        if damage >= self.health:
            return self.die()
        else:
            self.health -= damage
            return False

    def die():
        print(f"{self.name} has died, dropping {self.moeny}g")
        return [self.money, self.inventory, self.armor]

    def get_current_weight(self):
        total = 0
        for i in self.inventory:
            total += i.weight
        return total

    def inv_add(self, item):
        if self.get_current_weight + item.weight > self.inv_max_weight:
            return False
        else:
            self.inventory.append(item)
            return True
            
    def inv_remove(self, item_index):
        if item_index >= len(self.inventory):
            return False
        del self.inventory[item_index]
        return True

