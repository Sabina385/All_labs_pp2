import os 

path=r"C:\Users\ACER\Desktop\All_labs_PP2\labs\labs6\dir_andf_iles_md"

path_bool=os.access(path, os.F_OK)

if path_bool==False:
     print("Path does not exist")
elif path_bool == True:
     print("Directories:", ', '.join([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]))
     print("Files:", ', '.join([name for name in os.listdir(path) if  os.path.isfile(os.path.join(path, name))]))