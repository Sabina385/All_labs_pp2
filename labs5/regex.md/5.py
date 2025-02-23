import re
pattern= r"\b\w*a\w*b\b"
my_text="Today i am ot reading the book,because i just didnt want to, arab aaab a1234b aiibl kebab"
print(re.findall(pattern,my_text))