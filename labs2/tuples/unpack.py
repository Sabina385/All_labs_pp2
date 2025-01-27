fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)#apple banana cherry

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)#apple
print(yellow)#banana
print(red)#['cherry', 'strawberry', 'raspberry']

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(*green, tropic, red) = fruits
print(green) #['apple', 'mango', 'papaya']
print(tropic)#pineapple
print(red)#cherry


