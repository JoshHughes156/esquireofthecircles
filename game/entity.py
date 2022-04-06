from dialog import Dialog

class Entity:
    
    def __init__(self, name, health, location="", inventory=list(), armor=list(), money=0, inv_max_weight=0, weapon=0, hostile=False):
        self.name = name # The name of the current entity
        self.health = health # The health of the current entity
        self.location = location # Where in the world the entity is located
        self.inventory = inventory # The items currently on the entity
        self.armor = armor # The gear items currently equiped on the entity
        self.money = money # The money currently on the entity
        self.inv_max_weight = inv_max_weight # The max weight for the inventory
        self.hostile = hostile # Whether or not this entity will engage a fight
        self.weapon = weapon

    def take_damage(self, damage): # Allows the entity to take damage and die if the health is less than 0
        self.health -= damage
        if self.health <= 0: # If the damage would cause death
            self.health = 0
            return self.die()
        else:
            return False # Returns false as the entity didn't die

    def die(self):
        print(f"{self.name} has died, dropping {self.money}g")
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

class NPC(Entity):

    def __init__(self, name, dialog_location, dialog_path='dialog/'):
        self.name = name
        self.dialog_location = dialog_location
        self.dialog_path = dialog_path
        self.dialog = Dialog()
        self.hostile = False

    def load(self):
        generated_text = Dialog.load_from_file(self.dialog_location, dialog_path=self.dialog_path)
        self.dialog.text = generated_text[0]
        self.dialog.children = generated_text[1]
