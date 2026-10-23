with open("student.txt", "r") as f:
    for line in reversed(f.read().splitlines()):
        print(line)