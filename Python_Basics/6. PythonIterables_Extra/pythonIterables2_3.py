my_list = []
list_len = int(input("Enter how many numbers you want to check: "))

for i in range (1, list_len+1):
    number = int(input(f"Enter the number {i}: "))
    my_list.append(number)

lowest_number = my_list[0]

for i in range(list_len):
    if lowest_number > my_list[i]:
        lowest_number = my_list[i]

print(f"The lowest number in the list is {lowest_number}")