from datetime import date

class User:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth


    @property
    def age(self):
        today = date.today()
        has_not_passed = (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)

        return today.year - self.date_of_birth.year - has_not_passed


    @property
    def is_adult(self):
        return self.age >= 18


def legal_age(func):
    def wrapper(user):
        if not user.is_adult:
            raise ValueError(f"{user.name} need to be of legal age")
        return func(user)

    return wrapper

@legal_age
def buy_alcohol(user):
    return f"{user.name}, enjoy the alcohol"

try:
    client = User("Carlos", date(2006, 4, 3))
    print(buy_alcohol(client))
except ValueError as e:
    print(e)
