def repeat_twice(func):
    def wrapper(name):
        print(func(name))
        return func(name)

    return wrapper

@repeat_twice
def hello(name :str) -> str:
    return(f"Hola {name}")

print(hello("Ken"))
