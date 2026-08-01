# 15.	Duplicate Characters 
# 	Print all duplicate characters in a string. 

s = input("Enter a string: ")

seen = set()
dups = []
for ch in s:
	if ch in seen:
		if ch not in dups:
			dups.append(ch)
	else:
		seen.add(ch)

if dups:
	print("Duplicate characters:", ' '.join(dups))
else:
	print("No duplicate characters found.")
