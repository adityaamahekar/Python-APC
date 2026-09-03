#Single Inheritancce

class single():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(single):
    def __init__(self, name, age, id):
        single.__init__(self, name, age)
        self.id = id

    def display_student(self):
        self.display()
        print(f"Student ID: {self.id}")

print("----|| Student Details ||----")
print("--------------------------------------")

s=Student("Aditya", 20, "S12")
s1=Student("Om",19,"S7")

s.display_student()
print("--------------------------------------")
s1.display_student()