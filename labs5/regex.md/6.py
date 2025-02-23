import re
pattern = r"[ .,]" # класс символов.
replacement = ":"
text="The ability to learn new things is a valuable asset."
new_text = re.sub(pattern, replacement, text)
print(new_text)