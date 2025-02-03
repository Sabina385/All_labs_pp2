class Shape:
    def calculate_area(self):
        return 0

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
        
    def calculate_area(self):
        return self.side_length ** 2
a = float(input("a:"))
if a<0:
    exit()
mysquare=Square(a)
print("Area :",mysquare.calculate_area()) 
myshape=Shape()
print("Another:",myshape.calculate_area())   
           
    