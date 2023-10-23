import re

text = "The quick brown fox"
pattern = r"brown"

x = re.findall(pattern, text)

if x:
    print("Pattern found:", x)
else:
    print("Pattern not found")