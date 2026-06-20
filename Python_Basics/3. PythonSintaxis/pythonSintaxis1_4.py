print("Enter 3 differents numbers and we give you back the highest one")

high_number = int(input(f"Please enter the 1 number: "))

for i in range(2,4):
    number = int(input(f"Please enter the {i} number: "))
    if number > high_number:
        high_number = number
    else:
        high_number = high_number

print(f"The highest number is {high_number}")
