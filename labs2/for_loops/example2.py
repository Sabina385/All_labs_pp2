for x in range(2, 6):
  print(x) # 2 3 4 5
  
  
for x in range(2, 30, 3):
  print(x)   # 2 5 8 11 14 17 20 23 26 29

for x in range(6):
  print(x) #  0 1 2 3 4 5
else:
  print("Finally finished!")  # Finally finished!
  
for x in range(6):
  if x == 3: break
  print(x) # 0 1 2
else:
  print("Finally finished!") #NOT be executed 