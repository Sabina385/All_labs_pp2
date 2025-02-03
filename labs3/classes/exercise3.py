class Shape:
    def area_rectangle(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length 
        self.width=width 
    def area_rectangle(self):
        return self.length *  self.width   
a = float(input("a:"))
b = float(input("b:"))  
if a<0 or b<0:
    exit()
myrectangle=Rectangle(a,b)
print("Area :",myrectangle.area_rectangle())     
    