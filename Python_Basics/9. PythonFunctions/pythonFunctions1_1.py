
def print_hello():
    print("Hello ")
    return print_world()


def print_world():
    print("World")


def main():
    print_hello()


if __name__ == "__main__":
    main()