import time

number=int(input())
milsec=int(input())
sec=milsec/1000
time.sleep(sec)
sqrt=number **0.5
txt = 'Square root of {fnum} after {fsec} is {fsqrt}'.format(fnum = number, fsec = milsec, fsqrt = sqrt)
print(txt)