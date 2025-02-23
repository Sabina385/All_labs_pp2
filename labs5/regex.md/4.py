import re
pattern= r"[A-Z][a-z]+"
my_text="Today i am Not reading THe book,because i just didnt want to"
print(re.findall(pattern,my_text))