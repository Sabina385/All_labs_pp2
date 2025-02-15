def squares(a, b):
  for i in range(a, b + 1):
    yield i * i
a = int(input("enter a number a:")) 
b = int(input("enter a number b:")) 
square_generator = squares(a, b)
for square in square_generator:
  print(square,end=" ")