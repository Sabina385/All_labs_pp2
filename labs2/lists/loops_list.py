thislist = ["apple", "banana", "cherry"] #output apple
for x in thislist:                       #banana
  print(x)                               #cherry
  
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) # apple  banana  cherry
 
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]  

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)#['apple', 'banana', 'mango']
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist) #['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)#['hello', 'hello', 'hello', 'hello', 'hello']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)#['apple', 'orange', 'cherry', 'kiwi', 'mango']
