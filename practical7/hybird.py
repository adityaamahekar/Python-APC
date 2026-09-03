#Hybrid Inheritance

class student:
    def __init__(self, name, rno):
        self.name = name
        self.rno = rno

    def display_student(self):
        print(f"Student Name: {self.name}")
        print(f"Student Roll Number: {self.rno}")

class subject(student):
    def __init__(self, name, rno, subject_name): 

        student.__init__(self, name, rno)
        self.subject_name = subject_name

    def display_subject(self):
        self.display_student()
        print(f"Subject Name: {self.subject_name}")

class exam(student):
    def __init__(self, name, rno, marks):
        student.__init__(self, name, rno)
        self.marks = marks

    def display_exam(self):
        self.display_student()
        print(f"Marks: {self.marks}")

class result(subject, exam):
    def __init__(self, name, rno, subject_name, marks):
        subject.__init__(self, name, rno, subject_name)
        exam.__init__(self, name, rno, marks)

    def display_result(self):
        self.display_subject()
        print(f"Marks: {self.marks}")

print("----|| Student Result Details ||----")
print("--------------------------------------")

r = result("Aditya",12,"Python",90)

r.display_result()