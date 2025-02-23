import re
pattern= r"[a-z]+(?:_[a-z]+)+"
my_text="Today i_am not reading the book,because i_just_didnt want_to"
print(re.findall(pattern,my_text))