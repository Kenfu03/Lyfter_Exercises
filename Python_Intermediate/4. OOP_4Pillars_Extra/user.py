from abc import abstractmethod
from abc import ABC

class User(ABC):
    role = ""
    permissions = set()
    
    def __init__(self, name):
        self.name = name


    @abstractmethod
    def get_role(self, action):
        pass


    @abstractmethod
    def has_permission(self):
        pass


class AdminUser(User):
    role = "Admin"

    def has_permission(self, action):
        return True


    def get_role(self):
        return self.role


class RegularUser(User):
    role = "Regular"
    permissions = {
    "read",
    "check",
    "delete_account",
}

    def get_role(self):
        return self.role


    def has_permission(self, action):
        return action in self.permissions


boss = AdminUser("Carlos")
client = RegularUser("Allan")
print(f"User {boss.name} is {boss.get_role()}")
print(f"User {client.name} is {client.get_role()}")
print(boss.has_permission("delete"))
print(client.has_permission("read"))
