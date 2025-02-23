import re
pattern=r"[A-Z][^A-Z]*"
text = "PythonTutorialAndExercises"
result=re.findall(pattern, text)
print([word[1:] for word in result])