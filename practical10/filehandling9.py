vowels =0 
consonants = 0

with open("student.txt", "r") as f:
    for ch in f.read().lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)