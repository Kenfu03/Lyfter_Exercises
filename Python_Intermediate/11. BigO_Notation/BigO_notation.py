def print_numbers_times_2(numbers_list):
    # O(n)
    for number in numbers_list:
        print(number * 2)


def check_if_lists_have_an_equal(list_a, list_b):
    # O(a)
    for element_a in list_a:

        # O(a * b)
        for element_b in list_b:

            # O(1)
            if element_a == element_b:
                return True

    # O(1)
    return False


def print_10_or_less_elements(list_to_print):
    # O(1)
    list_len = len(list_to_print)

    # O(1)
    # The loop executes at most 10 times.
    for index in range(min(list_len, 10)):
        print(list_to_print[index])


def generate_list_trios(list_a, list_b, list_c):
    result_list = []

    # O(a)
    for element_a in list_a:

        # O(a * b)
        for element_b in list_b:

            # O(a * b * c)
            for element_c in list_c:

                # O(1)
                result_list.append(
                    f"{element_a} {element_b} {element_c}"
                )

    return result_list


def bubble_sort(arr):

    # O(1)
    comparisons = 0
    swaps = 0
    passes = 0

    # O(n)
    for n in range(len(arr) - 1):
        changes = False
        passes += 1

        # O(n^2)
        for i in range(len(arr) - 1 - n):

            # O(1)
            current = arr[i]
            next_value = arr[i + 1]

            comparisons += 1

            # O(1)
            if current > next_value:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                changes = True

        # O(1)
        if not changes:
            return arr

    return arr