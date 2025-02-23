import re
pattern = r"ab*"
text = "The ability to learn new things is a valuable asset."
print(re.findall(pattern, text))