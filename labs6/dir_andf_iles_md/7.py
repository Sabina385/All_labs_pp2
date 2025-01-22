try:
    with open(r"C:\Users\ACER\Desktop\All_labs_PP2\labs\Cat.txt", 'r') as cat, open(r"C:\Users\ACER\Desktop\All_labs_PP2\labs\Dog.txt", 'w') as dog:
        dog.write(cat.read())
    print("File copied!")
except FileNotFoundError:
    print("Error: source.txt not found.")
except Exception as e:
    print(f"An error occurred: {e}")
