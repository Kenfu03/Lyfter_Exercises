class Person():
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Bus():
    def __init__(self, brand, max_passengers):
        self.brand = brand
        self.max_passengers = max_passengers
        self.passengers = []


    def add_passenger(self, passenger):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(passenger)
            print(f"{passenger.name} got on the bus.")
        else:
            print("The bus is full.")


    def remove_passenger(self, passenger_name):
        for i, passenger in enumerate(self.passengers):
            if passenger.name == passenger_name:
                print(f"{passenger_name} got off the bus.")
                del self.passengers[i]
                return
        print(f"{passenger_name} is not on the bus.")
        

new_bus = Bus("Audi", 3)
person1 = Person("Juan", 20)
person2 = Person("Victor", 25)
person3 = Person("Diego", 15)
person4 = Person("Allan", 17)
new_bus.add_passenger(person1)
new_bus.add_passenger(person2)
new_bus.add_passenger(person3)
new_bus.remove_passenger("Victor")
new_bus.add_passenger(person4)


