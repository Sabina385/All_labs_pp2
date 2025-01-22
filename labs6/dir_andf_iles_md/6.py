import string
import os

if not os.path.exists("letters"):
    os.makedirs("letters")

for letter in string.ascii_uppercase:
    filename = os.path.join("letters", f"{letter}.txt")  
    with open(filename, 'w') as file:
        file.write(f"This is the file {letter}.txt\n") 

print("Files A.txt to Z.txt created in the 'letters' directory.")