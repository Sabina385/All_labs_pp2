thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)#{'cherry', 'apple'}

thisset = {"apple", "banana", "cherry"}# this method will remove a random item
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)#set()
