alphabets = digits = spaces = special = 0

with open("student.txt", "r") as f:
    for ch in f.read():
        if ch.isalpha():
            alphabets += 1
        elif ch.isdigit():
            digits += 1
        elif ch == " ":
            spaces += 1
        elif not ch.isspace():
            special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)