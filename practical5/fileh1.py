#read , write , append file

print("Read----------------------------------")
#read file
file = open("name.txt", "r")
content = file.read()
print("File Content:\n", content)
file.close()

print("Write----------------------------------")
#write file
file1 = open("name.txt", "w")
file1.write("This is the content.")
file1.close()


print("Append----------------------------------")
#append file
file2 = open("name.txt", "a")
file2.write("\nThis is another appended line.")
file2.close()