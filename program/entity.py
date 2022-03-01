
class Entity:
    
    def __init__(self, name. health, location, inventory=list(), armor=list(), money=0, inv_max_weight=0):
        self.name = name # The name of the current entity
        self.health = health # The health of the current entity
        self.location = location # Where in the world the entity is located
        self.inventory = inventory # The items currently on the entity
        self.armor = armor # The gear items currently equiped on the entity
        self.money = money # The money currently on the entity
        self.inv_max_weight = inv_max_weight # The max weight for the inventory

    def take_damage(self, damage): # Allows the entity to take damage and die if the health is less than 0
        if damage >= self.health: # If the damage would cause death
            return self.die()
        else:
            self.health -= damage
            return False # Returns false as the entity didn't die

    def die():
        print(f"{self.name} has died, dropping {self.moeny}g")
        return [self.money, self.inventory, self.armor] # List of all the drops of the entity

    def get_current_weight(self): # Gets the current weight of the inventory
        return sum([i.weight for i in self.inventory])

    def inv_add(self, item): # Adds an item to the inventory if it won't exceed the max weight
        if self.get_current_weight + item.weight > self.inv_max_weight:
            return False
        else:
            self.inventory.append(item)
            return True
            
    def inv_remove(self, item_index): # Removes an item
        if item_index >= len(self.inventory):
            return False
        del self.inventory[item_index]
        return True

