def return_generator(n):
    for i in range (n,-1,-1):#reversed(range(0,n+1))
        yield i
n=int(input("Enter a number n:")) 
generator = return_generator(n)
for numbers in generator:
    print(numbers,end=" ")      