import re
pattern = r"[h-o]"#set of characters
text = "Hello today hello today looooo"
print(re.findall(pattern, text))