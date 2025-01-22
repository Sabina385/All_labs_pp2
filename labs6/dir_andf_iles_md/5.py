my_list = [34, 23, 123, 123, 4.56]
filename = "my_text.txt"

try:
    with open(filename, 'w') as file:
        for item in my_list:
            file.write(str(item) + '\n')
    print(f"List successfully written to {filename}")
except Exception as e:
    print(f"An error occurred: {e}")
