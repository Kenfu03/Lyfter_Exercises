class Animal:
    specie = "Animal"

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} the {self.specie} says:"


class Dog(Animal):
    specie = "Dog"

    def speak(self):
        return super().speak() + " Guau Guau Guau!"


class Cat(Animal):
    specie = "Cat"

    def speak(self):
        return super().speak() + " Miau Miau Miau!"


dog = Dog("Whiskey")
cat = Cat("Paquis")

print(dog.speak())
print(cat.speak())