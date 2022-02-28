entity:
- name: str
- health: int
- inventory: item[]
- money: int
- armor: gear[]
: takedamage(damage: int): bool
: die(): void
- position: location

item:
- name: str

weapon(item):
- damage: int

gear(item):
- defensepoints: int
- place: str

location:
- name: str
- neighbours: location[]
