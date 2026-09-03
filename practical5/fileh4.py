#using wb+ , ab+ , rb

print("Using rb---------------------------------")
with open("name.txt", "rb") as file:
    content = file.read()
    print("\nFile Contents:", content)

print("Using wb+---------------------------------")
with open("name.txt", "wb+") as file1:
    file1.write(b"This is the 1st content inserted.")
    file1.seek(0)
    content1 = file1.read()
    print("File Content after write:\n", content1)

print("\nUsing ab+---------------------------------")
with open("name.txt", "ab+") as file2:
    file2.write(b"\nThis is another appended line.")
    file2.seek(0)
    content2 = file2.read()
    print("File Content after append:\n", content2)