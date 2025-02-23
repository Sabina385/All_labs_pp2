import re
pattern = r"\\."
text = "Hello today hello today looooo. "
print(re.findall(pattern, text))