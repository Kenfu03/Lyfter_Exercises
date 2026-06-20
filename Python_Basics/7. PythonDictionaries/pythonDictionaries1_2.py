list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

final_dict = {}

for i in range(len(list_a)):
    final_dict[list_a[i]] = list_b[i]

print(final_dict)