class Rectangle:
    def __init__(self, width, height):
        try:
            self.width = float(width)
            self.height = float(height)
        except ValueError:
            raise ValueError("Width and height must be numbers.")

        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive numbers.")


    def get_area(self):
        return self.width * self.height


    def get_perimeter(self):
        return 2 * (self.width + self.height)



if __name__ == "__main__":
    print("\nWelcome, lest create a Rectangle.")
    try:
        width = input("Plase enter rectangle width: ")
        height = input("Plase enter rectangle height: ")
        rectangle = Rectangle(width, height)
        print(f"The rectangle area is: {rectangle.get_area()}")
        print(f"The rectangle perimeter is: {rectangle.get_perimeter()}")
    except KeyboardInterrupt as e:
        print(e)
    except ValueError as e:
        print(e)
