def validate_number_list(func):
    def wrapper(arr):
        if not isinstance(arr, list):
            raise TypeError("No support non-list input")
        if len(arr) == 0:
            raise ValueError("Empty list!")
        if not all(isinstance(n, (int, float)) for n in arr):
            raise ValueError("All arguments must be numbers.")

        return func(arr)

    return wrapper


@validate_number_list
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


if __name__ == "__main__":
    try:
        my_list = []
        result = bubble_sort(my_list)
        print(result)

    except ValueError as e:
        print(e)

