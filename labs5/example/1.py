import re
pattern = r"a.c"
text = "abc aac axc a1c"
print(re.findall(pattern, text))