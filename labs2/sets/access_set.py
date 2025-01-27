thisset = {"apple", "banana", "cherry"}
print(thisset)#{'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)#{'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)#{True, 2, 'banana', 'cherry', 'apple'} The values True and 1 are considered the same value in sets, and are treated as duplicates:

myset = {"apple", "banana", "cherry"}
print(type(myset))#<class 'set'>

thisset = set(("apple", "banana", "cherry"))
print(thisset)#{'banana', 'apple', 'cherry'}
# Note: the set list is unordered, so the result will display the items in a random order.

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)#False