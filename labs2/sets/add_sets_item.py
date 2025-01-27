thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)#{'banana', 'cherry', 'apple', 'orange'}

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)#{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)#{'banana', 'cherry', 'apple', 'orange', 'kiwi'}