import re
pattern = r"^Hello"
text = "Hello today we write a new topic"
print(re.findall(pattern, text))