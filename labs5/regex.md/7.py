import re
pattern = r"[_]" # класс символов.
replacement = ""
text="_The ability to_learn new_things is a_valuable asset."
new_text = re.sub(pattern, replacement, text)
print(new_text)
