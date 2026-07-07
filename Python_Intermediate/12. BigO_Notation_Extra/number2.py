def linear_search(my_list, target):
    # O(n)
    for item in my_list:

        if item == target:
            return True

    return False


def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1

    # O(log n)
    while low <= high:
        mid = (low + high) // 2

        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


#¿Cuál es la complejidad de cada algoritmo?
# 1. O(n) 
# 2. O(log n)

#¿En qué condiciones conviene usar cada uno?
# 1. If list is unsorted, small and not to many searches
# 2. If list is sorted, large, for many searches

#¿Qué pasa si la lista no está ordenada?
# 1. Works fine, need more iterations, but find the result
# 2. Breaks, basically binary have left < mid < right, but the list is not sorted
# don't find the target