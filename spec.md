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
