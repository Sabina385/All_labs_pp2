import os

path = r"C:\Users\ACER\Desktop\All_labs_PP2\labs\labs6\dir_andf_iles_md\my_text.txt"

try:
    with open(path, 'r') as file:
       lines=[line for line in file if line.strip()]
    print("len of my_txt file:",len(lines))
except FileNotFoundError:
    print(f"Error: File not found at path: {path}")
 