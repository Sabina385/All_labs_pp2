import re
pattern = r"ll+"
text = "Hello today hello today looooo"
print(re.findall(pattern, text))