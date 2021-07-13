class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is a working")

class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def debug(self):
        print(f"{self.name} is debugging")

    #   overriding
    def work(self):
        print(f"{self.name} is coding")

class Designer(Employee):
    def draw(self):
        print(f"{self.name} is drawing")

    #   overriding
    def work(self):
        print(f"{self.name} is designing")

se = SoftwareEngineer("Max", 25, 4000, "Junior")
print(se.name, se.age)
se.work()
se.debug()

print()

d = Designer("Philip", 27, 1000)
print(d.name, d.age)
d.work()
d.draw()

print()

#   Polymorphism
employees = [SoftwareEngineer("Pushpa", 21, 6000, "Junior"), SoftwareEngineer("Lisa", 30, 9000, "Senior"), Designer("Philip", 27, 7000)]

#   work is called on the specific implementation of the child class
def motivate_employee(employees):
    for employee in employees:
        employee.work()
        print()

motivate_employee(employees)
