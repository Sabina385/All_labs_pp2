import re
pattern = r"w*"
text = "Hello today we write a new topic"
print(re.findall(pattern, text))