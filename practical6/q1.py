print("Normal Function:")
def add(a,b):
    return a+b
print("Addition:",add(1,6))

print("\n-------------------------------\n")

print("Function with default argument:")
def greet(name="Aditya"):
    print("Hello",name)
greet()
greet("Om")

print("\n-------------------------------\n")

print("Lambda function:")
square=lambda x : x*x
print("square", square(5))

print("\n-------------------------------\n")

print("Lambda function with 2 argument:")
multipy=lambda a,b : a*b
print("Multiplication:",multipy(3,5))