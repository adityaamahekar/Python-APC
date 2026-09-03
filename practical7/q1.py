# Demonstrate a class,object, constructor, and destructor.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Constructor is called:")
        print("name:",self.name)
        print("age:",self.age)

    def __del__(self):
        print("Destructor is called:")
        print("name:",self.name)
        print("age:",self.age)

name=input("Enter name:")
age=int(input("Enter age:"))

p = Person(name, age)
del p