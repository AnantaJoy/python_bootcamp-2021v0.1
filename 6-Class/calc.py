
class calc():
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def sum(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1 / self.num2
    
    def remainder(self):
        return self.num1 % self.num2
    
    def squar(self):
        return self.num2 * self.num2
    

x = calc(21,5)
print(dir(calc))
print(x.squar())
