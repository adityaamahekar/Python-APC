# Multilevel Inheritance

class student:
    def __init__(self, name, rno, password):
        self.name = name          # Public variable
        self._rno = rno           # Protected variable
        self.__password = password # Private variable

    def display_student(self):
        print("Name:", self.name)
        print("Roll Number:", self._rno)

    def display_private(self):
        print("Password:", self.__password)


class subject(student):
    def __init__(self, name, rno, password, subject_name):
        super().__init__(name, rno, password)
        self.subject_name = subject_name

    def display_subject(self):
        self.display_student()
        print("Subject Name:", self.subject_name)


class exam(subject):
    def __init__(self, name, rno, password, subject_name, marks):
        super().__init__(name, rno, password, subject_name)
        self.marks = marks

    def display_exam(self):
        self.display_subject()
        print("Marks:", self.marks)

e = exam("Aditya", 101, "pass123", "Python", 85)

e.display_exam()

e.display_private()