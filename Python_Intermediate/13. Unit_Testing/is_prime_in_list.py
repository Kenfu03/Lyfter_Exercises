def list_creation(list_size:int):
    list : number = []

    for i in range (1, list_size+1):
        number = int(input(f"Enter the number {i}: "))
        list.append(number)

    return list

def is_prime(number:int):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
            
    return True

def is_prime_in_list(numbers:list[int]):
    final_list:list[int] = []
    for number in numbers:
        if is_prime(number): final_list.append(number) 
    return final_list


if __name__ == "__main__":
    try:
        list_len = int(input("Enter how many numbers you want to check: "))
        print(is_prime_in_list(list_creation(list_len)))
    except ValueError as e:
        print(e)

