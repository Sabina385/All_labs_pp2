import os
path = r"C:\Users\ACER\Desktop\All_labs_PP2\labs\labs6\dir_andf_iles_md"
exists = os.path.exists(path)
readable = os.access(path, os.R_OK)
writable = os.access(path, os.W_OK)
executable = os.access(path, os.X_OK)

print(f"Exists: {exists}")
print(f"Readable: {readable}")
print(f"Writable: {writable}")
print(f"Executable: {executable}")