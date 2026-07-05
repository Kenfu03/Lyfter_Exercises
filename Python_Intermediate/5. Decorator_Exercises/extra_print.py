
def extra_information(func):
    def wrapper(*args):
        for arg in args:
            print(arg)
        return(f"Decorator result: {func(*args)}")

    return wrapper


@extra_information
def random_function(*args):
    return sum(args) / len(args)

print(random_function(1, 50, 67, 54, 34, 22, 57, 75, 755, 4, 65))