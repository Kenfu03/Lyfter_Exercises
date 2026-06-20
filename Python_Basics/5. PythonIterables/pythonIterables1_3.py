my_list = [4, 3, 6, 1, 7, 9, 12, 50]
last_index = len(my_list)-1

temp = my_list[last_index]
my_list[last_index]= my_list[0]
my_list[0] = temp

print(my_list)
