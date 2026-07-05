def repeat_twice(func):
    def wrapper(name):
        return func(name) + "\n" + func(name)
    return wrapper

@repeat_twice
def hello(name :str) -> str:
    return(f"Hello {name}")

print(hello("Ken"))
