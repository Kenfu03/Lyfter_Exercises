def bubble_sort_2(arr):
    for n in range(len(arr) - 1):
        changes = False

        for i in range(len(arr) - 1, n, -1):
            current = arr[i]
            prev_value = arr[i - 1]

            if current < prev_value:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                changes = True

        if not changes:
            return arr

    return arr

my_list = [8, 9, 10, 15, -12, -16, 20, 76]
print(bubble_sort_2(my_list))
