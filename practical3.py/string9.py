# 8. Frequency of a Character
# Find the number of times a specified character appears in a string.
from collections import Counter

text = input("Enter a string: ")

frquencies = Counter(text)

print(dict(frquencies))

