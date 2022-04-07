entity:
- name: str
- health: int
- inventory: item[]
- inv_max_weight: int
- money: int
- armor: gear[]
: takedamage(damage: int): bool
: die(): void
- position: location
: inv_add(item: item): bool
: inv_remove(item: item): bool
: get_inv_weight(): int

item:
- name: str
- weight: int

weapon(item):
- damage: int

gear(item):
- defensepoints: int
- place: str

location:
- name: str
- neighbours: location[]


game manager:
get data about current location
present data

armor slots:
helmet (20% * (1 - piece armor points/50))
chestplate (50% * (1 - piece armor points/70))
pants (20% * (1 - piece armor points/35))
boots (10% * (1 - piece armor points/20))

damage types: (x0.5 for weakness, x1.5 for strength)
fire: weak to water
water: weak to air
air: weak to fire

damage maths:
final damage = round(total from each piece * damage scaling factor)
damage on each piece:
damage * type modifier * (protection contribution from piece * (piece armor stat/total possible armor points))

Town Square:
- town guard - dialog relating to how he's not fighting the orcs in the south
- salesman - dialog about need to get in more stock

Tavern:
- Bartender - dialog relating to the ale shipments not arriving due to the orcs
- Drunkard - Compare the player to an orc

Woods:
- Goblin - "Ndichakuuraya iwe munhu anetsvina"