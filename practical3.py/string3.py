# 2.	Character Count 
# Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 

ch = input("Enter a String: ")

vowel = 0
consonant = 0
digit = 0
space = 0
schar = 0

for i in ch:
    if i.isalpha():
        if i.lower() in 'aeiou':
            vowel += 1
        else:
            consonant += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    else:
        schar += 1

print("Vowels:", vowel)
print("Consonants:", consonant)
print("Digits:", digit)
print("Spaces:", space)
print("Special characters:", schar)