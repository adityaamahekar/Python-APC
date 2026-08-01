# 4.	 Palindrome Check 
# ●	Check whether the entered string is a palindrome. 

s = input("Enter a String: ")

rev = ''.join(reversed(s))
print("revers of a string:",rev)

if s == rev:
    print("String is palindrome")
else:
    print("String is not palindrome")