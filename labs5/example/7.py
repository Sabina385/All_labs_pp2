import re
pattern = r"lo{4}"#exact occurences
text = "Hello today hello today looooo"
print(re.findall(pattern, text))