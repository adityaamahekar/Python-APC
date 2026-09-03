#hirarchical inheritance

class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_employee(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.id}")

class manager(employee):
    def __init__(self, name, id, department):
        employee.__init__(self,name, id)
        self.department = department

    def display_manager(self):
        self.display_employee()
        print(f"Department: {self.department}")

class salary(employee):
    def __init__(self, name, id, salary):
        employee.__init__(self,name, id)
        self.salary = salary

    def display_salary(self):
        self.display_employee()
        print(f"Salary: {self.salary}")

print("----|| Employee Details ||----")
print("--------------------------------------")

s =salary("Aditya", 20, 50000)
s.display_salary()