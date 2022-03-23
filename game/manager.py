from entity import Entity, NPC
from location import Location


# Instaniate some NPCs
guard = NPC("Guard", "townguard1.txt", dialog_path="dialog/")
salesman = NPC("Salesman", "empty.txt")
bartender = NPC("Bartender", "empty.txt")

# Call the load on all the npcs
guard.load()
salesman.load()
bartender.load()

# Initalise locations
locations = []
town_square = Location("Town square", npcs=[guard, salesman])
tavern = Location("Tavern", npcs=[bartender])

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
    print(f"\nYou are currently in {player.location.name}")

    print("\nWhat would you like to do?:\n\
           1) View nearby locations\n\
           2) View nearby NPCs\n\
           3) Exit game")

    choice = input("Please enter your choice: ")
    while choice not in ["1", "2", "3"]:
        print("Please enter a valid choice")
        choice = input("Please enter your choice: ")

    if choice == "1":
        for i, n in enumerate(player.location.get_neighbours()):
            print(f"{i+1}: {n.name}")
        l = input("Would you like to travel to any of these locations (0 to remain in current location): ")
        if int(l) <= len(player.location.get_neighbours()) and int(l) > 0:
            player.location = player.location.get_neighbours()[i-1]

        continue
    elif choice == "2":
        for i, n in enumerate(player.location.npcs):
            print(f"{i+1}: {n.name}")
        l = input("Would you like to talk to any of these people: ")
        if int(l) <= len(player.location.npcs) and int(l) > 0:
            d = player.location.npcs[int(l)-1].dialog
            #__import__('sys').exit()
            while d != "END":
                opts = []
                for line in d.text:
                    if '>' not in line:
                        print(line)
                    else:
                        opts.append(line)

                if len(opts) == 0:
                    break

                for i, v in enumerate(opts):
                    print(f"{i+1}{v}")

                choice = -1
                while choice not in [x+1 for x in range(len(opts))]:
                    choice = int(input("Please enter your choosen dialog: "))

                d = d.children[choice-1]

            continue # TODO add dialog interaction here

        continue
    elif choice == "3":
        print("\nBYE\n")
        break
