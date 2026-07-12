def list_creation(list_size:int):
    list : number = []
    
    for i in range (1, list_size+1):
        number = int(input(f"Enter the number {i}: "))
        list.append(number)

    return list


def sum_list(list:list[int]):
    result = 0

    for num in list:
        result += num

    return result


if __name__ == "__main__":
    try:
        list_len = int(input("Enter how many numbers you want to sum: "))
        my_list = list_creation(list_len)
        print(f"The sum of all the numbers in the list is: {sum_list(my_list)}")
    except ValueError as e:
        print(e)