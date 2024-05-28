import random

class Brawler:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        
    def take_damage(self, damage):
        self.health -= damage
        
    def is_alive(self):
        return self.health > 0

def battle(brawler1, brawler2):
    while brawler1.is_alive() and brawler2.is_alive():
        damage1 = random.randint(1, brawler1.attack)
        damage2 = random.randint(1, brawler2.attack)
        
        brawler2.take_damage(damage1)
        brawler1.take_damage(damage2)
        
        print(f"{brawler1.name} attacks {brawler2.name} for {damage1} damage")
        print(f"{brawler2.name} attacks {brawler1.name} for {damage2} damage")
        print(f"{brawler1.name} health: {brawler1.health}")
        print(f"{brawler2.name} health: {brawler2.health}")
        print()
        
    if brawler1.is_alive():
        print(f"{brawler1.name} wins!")
    else:
        print(f"{brawler2.name} wins!")

# Creazione dei due brawlers
brawler1 = Brawler("Edgar", 150, 15)
brawler2 = Brawler("Leon", 110, 20)

# Inizio battaglia
battle(brawler1, brawler2)