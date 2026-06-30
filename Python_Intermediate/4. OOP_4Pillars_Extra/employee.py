class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.salary = salary


    @property
    def salary(self):
        return self.__salary


    @property
    def name(self):
        return self.__name


    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("The salary value cannot be negative")
        self.__salary = value


    def promote(self, porcentage):
        self.salary += self.salary * porcentage

try:
    employee = Employee("Jason",2500)
    print(employee.name)
    print(employee.salary)
    employee.promote(-2)
    print(employee.salary)

except ValueError as e:
    print(e)
