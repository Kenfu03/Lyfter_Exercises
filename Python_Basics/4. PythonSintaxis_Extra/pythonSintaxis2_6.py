number = int(input("Enter a number between 1 - 10 to give you the multiplication table: "))

for i in range(1, 13):
    print(f"{number} x {i} = {number*i}")
