#smallest of three numbers

a=int(input("Enter value of A:"))
b=int(input("Enter value of B:"))
c=int(input("Enter value of C:"))

if a<b and a<c :
    print("A is smallest :", a)
elif b<c:
    print("B is smallest :", b)
else:
    print("C is smallest :", c)