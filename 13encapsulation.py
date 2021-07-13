#   Encapsulation is the method of hiding data implementation
class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #   by convention, private instance attributes are prepended with an '__' but a '_' will be accessible outside (protected)
        self.__salary = None
        self._num_bugs_solved = 0

    #   getter
    @property
    def salary(self):
        return self.__salary

    #   setter
    @salary.setter
    def salary(self, value):
        self.__salary = value

    #   deleter
    @salary.deleter
    def salary(self):
        del self.__salary

    #   private function
    def __code(self):
        print(f"{self.name} is coding")

    #   destructor
    def __del__(self):
        print(f"{self.name} destructed")

se = SoftwareEngineer("Max", 25)

se.salary= 6000
print(se.salary)
del se.salary

del se

#   Abstraction is the mechanism of abstracting the internal structure, this is a consequent of polymorphism
