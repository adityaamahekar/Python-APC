#Multiple Inheritance

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_student(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")

class subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name

    def display_subject(self):
        print(f"Subject Name: {self.subject_name}")

class marks(student, subject):
    def __init__(self, name, age, subject_name, marks):
        student.__init__(self, name, age)
        subject.__init__(self, subject_name)
        self.marks = marks

    def display_marks(self):
        self.display_student()
        self.display_subject()
        print(f"Marks: {self.marks}")

print("----|| Student Marks Details ||----")
print("--------------------------------------")

m=marks("Aditya", 20, "AT", 95)
m.display_marks()

print("--------------------------------------")

m1=marks("Om", 19, "CN", 88)
m1.display_marks()