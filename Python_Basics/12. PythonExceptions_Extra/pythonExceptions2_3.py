my_list = ['10', 'manzana', '5.5', '3', 'n/a']

def add_data(data_list : list):
    total_sum : float = 0
    for item in data_list:
        try:
            number : float = float(item)
            print(f"Element {item} added")
            total_sum += number
        except ValueError:
            print(f"Impossible to add '{item}'")
    return total_sum


def main():
    print("Result: ")
    final_result : float = add_data(my_list)
    print(f"The final result is: {final_result}")

if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(f"Something goes wrong: {ex}")