numbers_list = []
high_number = 0


for i in range(1, 11):
    number = int(input(f"Enter the number {i}: "))
    numbers_list.append(number)

    if high_number < number:
        high_number = number

print(numbers_list)
print(f"The highest number is: {high_number}")