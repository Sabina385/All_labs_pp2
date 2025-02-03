def unique_elements(lst):
    unique_list = [] 
    for item in lst:
        if item not in unique_list:
            unique_list.append(item) 
    return unique_list

user_input = input("Enter a element: ")
lst = user_input.split() 
print("Unique elements: ", unique_elements(lst))