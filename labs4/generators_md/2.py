def even_generator(n):
    for i in range(0,n+1):
        if i%2==0:
            yield i
n= int (input("enter a number:"))            
generator= even_generator(n)
for even in generator:
    print (even)

          