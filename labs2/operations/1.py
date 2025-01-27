print(10 + 5) #15

x = 15
y = 2
print(x // y) #7

x = 5
x &= 3
print(x) #2 multiplication by bytes (в десятичной форме)

x = 5
x |= 3
print(x)#7 sum by bytes

x = 5 #(переводим в двоичную систему)
x ^= 3
print(x)#XOR output 6

print(~3)#output:-4
#The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).
#Inverted 3 becomes -4:
 #3 = 0000000000000011
#-4 = 1111111111111100

print(3 << 2)
#The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

#If you push 00 in from the left:
#3 = 0000000000000011 becomes 12 = 0000000000001100


print(x := 3) #(пресваевает значение к х и возвращает его) output 3
# ==	Equal	x == y	x=2 y=5 output: False
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y	

x = 5
print(x > 3 and x < 10) #output:True

x = 5
print(x > 7 or x < 5)#output False


