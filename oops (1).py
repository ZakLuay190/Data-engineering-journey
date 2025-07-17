class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # private

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary

emp = Employee("Ali", 51000)
print(emp.get_salary())
emp.set_salary(55000)
print(emp.get_salary())
