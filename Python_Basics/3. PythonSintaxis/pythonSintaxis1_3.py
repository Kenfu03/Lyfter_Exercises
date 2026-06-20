import random

random_number = random.randint(1, 10)
choose_number = int(input("Ingrese un numero del 1 a 10: "))

while (choose_number != random_number):
    choose_number = int(input("Fallaste, intentalo de nuevo: "))

print(f"Felicidades lo adivinaste, el numero era {random_number}")