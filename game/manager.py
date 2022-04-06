from sys import exit

from entity import Entity, NPC
from location import Location
from item import Weapon, Gear


# Instantiate some NPCs
guard = NPC("Guard", "townguard1.txt", dialog_path="dialog/")
salesman = NPC("Salesman", "empty.txt")
bartender = NPC("Bartender", "empty.txt")
generic_armor = [Gear("Leather Cap", 0, 3, "helmet"), Gear("Leather Chestplate", 0, 5, "chestplate"), Gear("Leather Pants", 0, 5, "pants"), Gear("Leather Boots", 0, 2, "boots")]
generic_sword = Weapon("Wooden broadsword", 0, 5)
drunkard = Entity("Drunkard", 12, armor=generic_armor, money=10, weapon=generic_sword, hostile=True)

# Call the load on all the npcs
guard.load()
salesman.load()
bartender.load()

# Initalise locations
locations = []
town_square = Location("Town square", npcs=[guard, salesman])
tavern = Location("Tavern", npcs=[bartender, drunkard])

# Set all the neighbours of the locations
town_square.set_neighbours([tavern])
tavern.set_neighbours([town_square])

# Save them all to a list of locations
locations.append(town_square)
locations.append(tavern)


# Instantiate the player
name = input("What would you like your character's name to be?: ")

player = Entity(name, 25, town_square, weapon=generic_sword)

def game_over(): # When the player has died, could be changed
    print("\nYou have died, thank you for playing!")
    exit()

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

    print('')

    if choice == "1":
        for i, n in enumerate(player.location.get_neighbours()):
            print(f"{i+1}: {n.name}")
        print("0: Exit menu")
        l = input("Would you like to travel to any of these locations: ")
        if int(l) <= len(player.location.get_neighbours()) and int(l) > 0:
            player.location = player.location.get_neighbours()[i-1]

        continue
    elif choice == "2":
        for i, n in enumerate(player.location.npcs):
            if not n.hostile:
                print(f"{i+1}: {n.name}")
            else:
                print(f"{i+1}: {n.name} (battle)")
        print("0: Exit menu")
        l = input("Would you like to talk to any of these people: ")
        if int(l) <= len(player.location.npcs) and int(l) > 0:
            if not player.location.npcs[int(l)-1].hostile:
                d = player.location.npcs[int(l)-1].dialog
                print('\n')
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
            else:
                #continue # Added the battle code in here
                enemy = player.location.npcs[int(l)-1]
                while True:
                    # Player go
                    choice = ""
                    print("\nWhat will you do?\n1) Attack\n2) Flee")
                    while choice not in ["1", "2"]:
                        choice = input("Please enter your choice: ")
                    
                    print('\n')

                    if choice == "1":
                        damage = Weapon.damage_calc(player.weapon, enemy.armor)
                        print(f"You attack the {enemy.name} with your {player.weapon.name}, dealing {damage} damage")                       
                        drops = enemy.take_damage(damage)
                        if not drops:
                            print(f"The enemy is now on {enemy.health} health")
                        else:
                            player.money += drops[0] # Add dropped items and armor here
                            print(f"\nYou now have {player.money}g")
                            player.location.npcs.remove(player.location.npcs[int(l)-1])
                            break
                    elif choice == "2":
                        print(f"You drop {player.money*0.2}g whilst fleeing, you now have {player.money*0.8}g")
                        player.money *= 0.8
                        break

                    print('\n')

                    damage2 = Weapon.damage_calc(enemy.weapon, player.armor)
                    print(f"The {enemy.name} attacks you with their {enemy.weapon.name}, dealing {damage2} damage")
                    player.health -= damage2
                    if player.health > 0:
                        print(f"You are now on {player.health} health")
                    else:
                        game_over()

        continue
    elif choice == "3":
        print("\n########################\n|Thank you for playing!|\n########################")
        break
