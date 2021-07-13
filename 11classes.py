#   class
class SoftwareEngineer:
    #   class attribute
    alias = "Keyboard Magician"

    # double under methods / d-under methods
    def __init__(self, name, age, level, salary):
        #   instance attributes
        self.name = name
        self.age = age
        self.level =level
        self.salary = salary

    #   instance method
    def code(self):
        print(f"{self.name} is writing code.")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")

    #   this method is called when the object is converted to string
    def __str__(self):
       information = f"name = {self.name}, age = {self.age}, level = {self.level}"
       return information

    def __eq__(self, other):
       return self.name == other.name and self.age == other.age
    
    @staticmethod
    def entry_salary(age):
        if age < 23: 
            return 5000
        if age < 27: 
            return 7000
        return 9000

#   instance
se1 = SoftwareEngineer("John Doe", 20, "Junior", 5000)

se2 = SoftwareEngineer("Lisa Doe", 22, "Senior", 7000)

print(se1.name, se1.age)
print(se1.alias)
print(SoftwareEngineer.alias)

se1.code()
se2.code()

se1.code_in_language("C++")

print(se1)

se3 = SoftwareEngineer("John Doe", 20, "Junior", 5000)
print (se1 == se3)

print(se1.entry_salary(23))
