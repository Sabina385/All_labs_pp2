def spy_game(nums):
    code = [0, 0, 7] 
    index = 0  
    
    for num in nums:
        if num == code[index]:
            index += 1  
            if index == len(code):
                return True
    return False
user_input=input("enter a numbers:")
nums=list(map(int,user_input.split()))
print (spy_game(nums))

#print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # → True
#print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # → True
#print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # → False