class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def get_area(self):
        return self.width * self.height

    
    def get_perimeter(self):
        return 2 * (self.width + self.height)


def ask_inputs(prompt):
    while True:
        try:
            number = float(input("Please enter rectangle " + prompt))

            if number > 0:
                return number

            print("Need to be a positive number")

        except ValueError:
            print ("Need to be a positive number")


if __name__ == "__main__":
    print("\nWelcome, lest create a Rectangle.")
    try:
        width = ask_inputs("width: ")
        height = ask_inputs("height: ")
        rectangle = Rectangle(width, height)
        print(f"The rectangle area is: {rectangle.get_area()}")
        print(f"The rectangle perimeter is: {rectangle.get_perimeter()}")
    except KeyboardInterrupt as e:
        raise(e)