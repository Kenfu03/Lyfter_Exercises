my_list = []
list_len = int(input("Enter how many numbers you want to check: "))
new_list = []

for i in range (1, list_len+1):
    number = int(input(f"Enter the number {i}: "))
    my_list.append(number)

average = sum(my_list) / len(my_list)

for num in my_list:
    if num > average:
        new_list.append(num)

print(f"The new list with numbers higher than {average} is {new_list}")