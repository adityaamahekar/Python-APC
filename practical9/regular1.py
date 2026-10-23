#regular experssion

import re

text = "Hello 123 World 456"

# 1. findall() 
print(re.findall(r"\d+", text))  

print("\n----------------------------------\n")

# 2. compile() 
pattern = re.compile(r"\d+")
print(pattern.findall(text))    

print("\n----------------------------------\n")

# 3. split() 
print(re.split(r"\s+", text))  

print("\n----------------------------------\n")

# 4. sub() 
print(re.sub(r"\d+", "X", text)) 

print("\n----------------------------------\n")

# 5. escape() 
print(re.escape("a+b"))         

print("\n----------------------------------\n")

# 6. search() 
match = re.search(r"\d+", text)
if match:
    print(match.group())    

   