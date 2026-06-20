my_list = []
list_len = int(input("Enter how many numbers you want to check: "))
counter = 0

for i in range (1, list_len+1):
    number = int(input(f"Enter the number {i}: "))
    my_list.append(number)

number_to_find = int(input("Enter the number to find: "))

for num in my_list:
    if num == number_to_find:
        counter += 1

print(f"The number {number_to_find} appears {counter} times")