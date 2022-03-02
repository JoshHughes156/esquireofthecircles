from entity import Entity
from location import Location

# Initalise locations
locations = []
town_square = Location("Town square")
tavern = Location("Tavern")

# Set all the neighbours of the locations
town_square.set_neighbours([tavern])
tavern.set_neighbours([town_square])

# Save them all to a list of locations
locations.append(town_square)
locations.append(tavern)

# Instantiate the player
name = input("What would you like your character's name to be?: ")

player = Entity(name, 10, town_square)

while True:

    # Get data about current location
    print(f"You are currently in {player.location.name}")

