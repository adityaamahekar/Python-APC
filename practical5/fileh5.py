#using rb, wb , ab

print("Using wb---------------------------------")
with open("name.txt", "wb") as f:
    f.write(b"This is the first content.")

print("Using rb---------------------------------")
with open("name.txt", "rb") as f:
    content = f.read()
    print("File Contents:", content)

print("Using ab---------------------------------")
with open("name.txt", "ab") as f:
    f.write(b"\nThis is appended content.")

print("Final read with rb-----------------------")
with open("name.txt", "rb") as f:
    final_content = f.read()
    print("File Contents after append:\n", final_content)