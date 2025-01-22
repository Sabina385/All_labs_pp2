text=input()

cnt1=0
cnt2=0

for i in text:
    if i.isupper():
        cnt1+=1
    elif i.islower():
        cnt2+=1
        

print(cnt1)
print(cnt2)
        