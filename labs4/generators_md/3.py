def my_generator(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
n=int (input("Enter a number:"))
divisible_by3and4= my_generator(n)
for numbers in divisible_by3and4:
    print (numbers,end=" ")        