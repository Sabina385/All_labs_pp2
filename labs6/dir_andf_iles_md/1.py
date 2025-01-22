import os

path=r"C:\Users\ACER\Desktop\All_labs_PP2\labs\labs6\dir_andf_iles_md"

print("All:", [name for name in os.listdir(path)]) #everything
print("Folders:", [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]) # only directories
print("Files:", [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]) # only files 

print("------------------------------------------------------------")


with os.scandir(path) as entries:
    all_items = []
    folders = []
    files = []

    for entry in entries:
        all_items.append(entry.name)
        if entry.is_dir():
            folders.append(entry.name)
        if entry.is_file():
            files.append(entry.name)

print(f"All: {', '.join(all_items)}")
print(f"Folder: {', '.join(folders) if folders else ''}")
print(f"File: {', '.join(files) if files else ''}")
