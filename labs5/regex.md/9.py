import re
pattern=r"[A-Z][^A-Z]*"
text = input()
print(re.findall(pattern, text))