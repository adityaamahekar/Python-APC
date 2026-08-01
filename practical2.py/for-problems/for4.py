# program that prints 1 2 4 8 16 32 .... 2^n

n = int(input("Enter n: "))
value = 1

for i in range(n + 1):
    print(value, end=" ")
    value =value * 2

