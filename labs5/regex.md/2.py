import re
pattern = r"ab{2,3}"
text = "The ability to abbbb abb learn new a things is a valuable asset."
print(re.findall(pattern, text)) 