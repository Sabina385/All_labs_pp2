import re

def camel_to_snake(text):
    # Added an underscore before each uppercase letter (except at the beginning)
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', text)
    return snake_case

text = "CamelCaseText"
print(camel_to_snake(text)) 