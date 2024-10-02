import random

class Character:
    #def __init__(self, name, hp, dps, defensa, mana, magic_dps, stamina, aguante, arcano, image)
    def __init__(self, name, hp, attack, image):
        self.name = name
        self.hp = hp
        self.attack = attack
        #self.defensa = defensa
        #self.mana = mana
        #self.magic_dps = magic_dps
        #self.stamina = stamina
        #self.aguante = aguante
        #self.arcano = arcano
        self.image = image

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0


class Player(Character):
    pass

class Enemy(Character):
    def generate_attack(self):
        return random.randint(self.attack -5, self.attack +5)