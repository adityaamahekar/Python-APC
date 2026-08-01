# 10. ASCII Values
# Display each character of a string along with its ASCII value.

s = input("Enter a string: ")

if s == "":
	print("No characters to display.")
else:
	for ch in s:
		print(f"{repr(ch)} : {ord(ch)}")

