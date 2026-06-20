number_list = []
is_30 = False

for i in range(3):
    number_list.append(int(input(f"Please enter the number {i}: ")))
    if number_list[i] == 30:
        is_30 = True

if sum(number_list) != 30 and not is_30:
    print("Incorrect")
else:
    print("Correct")

