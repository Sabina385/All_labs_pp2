import re
pattern = r"lllo$"
text = "Hello today we write a new topic lllo"
print(re.findall(pattern, text))