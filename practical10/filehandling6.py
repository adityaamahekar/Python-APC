with open("student.txt", "r") as f:
    print("Total words: ", len(f.read().split()))