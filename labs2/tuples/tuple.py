#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.
thistuple = ("apple", "banana", "cherry")
print(thistuple)#('apple', 'banana', 'cherry')

thistuple = ("apple",)
print(type(thistuple))#<class 'tuple'>
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))#<class 'str'>

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)#('apple', 'banana', 'cherry')