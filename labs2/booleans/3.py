print(bool("Hello"))#true
print(bool(15))#trure
print(bool([]))#false
print(bool(False))#false
print(bool(None))#false
print(bool(0))#false
print(bool(""))#false
print(bool(()))#false
print(bool(" "))#true
print(bool({}))#false

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #false

#def
def myFunction() :
  return True

print(myFunction())#True
#2
def myFunction() :
  return True

if myFunction():
  print("YES!") 
else:
  print("NO!")
#output:YES  

x = 200
print(isinstance(x, int))#True 