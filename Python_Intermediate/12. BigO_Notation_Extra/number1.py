def manual_add(number):
    result = 0
    # O(n)
    for i in range(1, number + 1):
        result += i

    # O(1)
    return result


def add_formula(number):
    # O(1)
    return number * (number + 1) // 2

#If the number is 1,000,000 I will user add_formula, because 
# O(n) grows with input size
# O(1) is constant all the time