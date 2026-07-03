class Flyable:
    def fly(self):
        print(f"{self.name} is flying in the sky.")


class FireBreather:
    def breathe_fire(self):
        print(f"{self.name} breathes a huge stream of fire!")


class Regenerator:
    def regenerate(self):
        self.health += 20
        print(f"{self.name} regenerated to {self.health} HP.")


class Dragon(Flyable, FireBreather, Regenerator):
    def __init__(self, name, health):
        self.name = name
        self.health = health


dragon = Dragon("Smaug", 100)
dragon.fly()
dragon.breathe_fire()
dragon.regenerate()