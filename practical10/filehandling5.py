with open("student.txt", "r") as f:
    print("Total lines:", sum(1 for line in f))