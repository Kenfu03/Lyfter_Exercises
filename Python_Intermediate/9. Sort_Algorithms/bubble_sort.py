def bubble_sort(arr):
    for n in range(len(arr) - 1):
        changes = False

        for i in range(0, len(arr) - 1 - n):
            current = arr[i]
            next_value = arr[i + 1]

            if current > next_value:
                arr[i],  arr[i + 1] = arr[i + 1], arr[i]
                changes = True

        if not changes:
            return arr

    return arr

my_list = [8, 9, 10, 15, -12, -16, 20, 76]
print(bubble_sort(my_list))

