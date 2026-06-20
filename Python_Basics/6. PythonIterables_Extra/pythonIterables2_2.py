my_list = []
list_len = int(input("Enter how many numbers you want to check: "))
all_positives = True

for i in range (1, list_len+1):
    number = int(input(f"Enter the number {i}: "))
    my_list.append(number)

for num in my_list:
    if num <= 0:
        all_positives = False
        break

if all_positives:
    print("All the elements are positives")
else:
    print("Atleast one number in the list is negative or zero")