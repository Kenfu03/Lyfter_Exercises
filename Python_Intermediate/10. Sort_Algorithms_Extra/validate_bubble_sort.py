def validate_number_list(func):
    def wrapper(list):
        if not all(isinstance(n, (int, float)) for n in list):
            raise ValueError("All arguments must be numbers.")

        return func(list)

    return wrapper


@validate_number_list
def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    passes = 0
    for n in range(len(arr) - 1):
        changes = False
        passes += 1

        for i in range(0, len(arr) - 1 - n):
            current = arr[i]
            next_value = arr[i + 1]
            
            comparisons += 1
            if current > next_value:
                arr[i],  arr[i + 1] = arr[i + 1], arr[i]
                changes = True
                swaps += 1

        if not changes:
            return {
                    "array": arr,
                    "comparisons": comparisons,
                    "swaps": swaps,
                    "passes": passes,
                }

    return {
            "array": arr,
            "comparisons": comparisons,
            "swaps": swaps,
            "passes": passes,
        }


if __name__ == "__main__":
    try:
        my_list = [8, 9, "Hola", 15, -12, -16, 20, 76]
        result = bubble_sort(my_list)
        print(f"""Sort array = {result["array"]}
Comparisons = {result["comparisons"]}
Swaps = {result["swaps"]}
Passes = {result["passes"]}""")

    except ValueError as e:
        print(e)

