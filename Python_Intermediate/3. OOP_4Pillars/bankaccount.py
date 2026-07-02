class BankAccount:
    balance = 0

    def add_money(self, amount):
        self.balance += amount


    def remove_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("No enough money.")


class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        self.min_balance = min_balance
        self.balance = min_balance


    def remove_money(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print(f"The minimum money in the Saving account is: S{self.min_balance}")


saves = SavingsAccount(1200)
print(saves.balance)
saves.add_money(900)
print(saves.balance)
saves.remove_money(1100)
print(saves.balance)


