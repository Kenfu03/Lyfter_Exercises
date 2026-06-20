my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_new_list = []

for i in range (len(my_list)):
    if my_list[i] % 2 == 0:
        my_new_list.append(my_list[i])

print(my_new_list)