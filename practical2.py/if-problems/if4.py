#largest of three numbers

a=int(input("Enter value of A:"))
b=int(input("Enter value of B:"))
c=int(input("Enter value of C:"))

if a>b and a>c :
    print("A is largest :", a)
elif b>c:
    print("B is largest :", b)
else:
    print("C is largest :", c)
    