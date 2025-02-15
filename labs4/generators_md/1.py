def my_generator(N):
    for i in range(N+1):
        yield i**2
N=int(input("Enter a number:"))        
generator= my_generator(N)
for square in generator:
    print(square,end=" ")
