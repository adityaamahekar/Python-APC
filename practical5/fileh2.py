#using read() , readline(), readlines() to read file

print("Using read()----------------------------------")
file = open("name.txt", "r")
content = file.read()
print("File Content:\n", content)
file.close()

print("Using readline()----------------------------------")
file1 = open("name.txt", "r")
line1 = file1.readline()
line2 = file1.readline()
print("Line 1:", line1)
print("Line 2:", line2)
file1.close()

print("Using readlines()----------------------------------")
file2 = open("name.txt", "r")
lines = file2.readlines()
print("All Lines:", lines)
file2.close()