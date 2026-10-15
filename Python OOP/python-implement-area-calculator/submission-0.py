import math

class AreaCalc:
    # TODO: Implement calculate method
    def __init__(self,length=None,width=None)->None:
        self.length=length
        self.width=width

    def calculate(self, length, width=None):
        if width is None:
            return round(math.pi * length ** 2, 2)
        else:
            return length * width
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
