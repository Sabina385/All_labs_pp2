import os

file_path = r"C:\Users\ACER\Desktop\All_labs_PP2\labs\labs6\dir_andf_iles_md\new_textfile.txt"

try:
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
    elif not os.access(file_path, os.W_OK):
        print(f"Error: No write access to {file_path}")
    else:
        os.remove(file_path)
        print(f"Successfully deleted {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")