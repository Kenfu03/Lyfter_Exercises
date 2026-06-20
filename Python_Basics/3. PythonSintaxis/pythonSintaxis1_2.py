name = input("Ingrese su nombre completo: ")
age = int(input("Ingrese su edad: "))
result = ""

if age < 2:
    result = "bebe"
elif age < 8:
    result = "niño"
elif age < 12:
    result = "preadolecente"
elif age < 19:
    result = "adolecente"
elif age < 40:
    result = "adulto joven"
elif age < 65:
    result = "adulto"
else:
    result = "adulto mayor"

print(f"{name} de {age} años esta dentro de {result}")