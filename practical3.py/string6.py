# 5.	Uppercase and Lowercase Count 
# ●	Count the number of uppercase and lowercase letters in a string. 

ch = input("Enter a string: ")

upper = 0
lower = 0

for i in ch:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

