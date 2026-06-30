class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_info(self):
        return f"{self.brand} ({self.year})"


class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors


    def get_info(self):
        sentence = super().get_info()
        return sentence + f"- Doors: {self.doors}"


class Motorcycle(Vehicle):
    def __init__(self, brand, year, bike_type):
        super().__init__(brand, year)
        self.bike_type = bike_type


    def get_info(self):
        sentence = super().get_info()
        return sentence + f"- Type: {self.bike_type}"


moto = Motorcycle("Yamaha", 2025, "Sport")
car = Car("Nissan", 2026, 4)
print(moto.get_info())
print(car.get_info())