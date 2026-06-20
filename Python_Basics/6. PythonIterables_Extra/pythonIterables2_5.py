my_list = []
new_list = []

for i in range (1, 6):
    word = str(input(f"Enter the word {i}: "))
    my_list.append(word)

for word in my_list:
    if len(word) > 4:
        new_list.append(word)

print(f"Old list {my_list}, new list with words longer than 4 letters is {new_list}")