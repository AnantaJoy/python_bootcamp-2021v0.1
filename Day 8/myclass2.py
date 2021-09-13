class Student:
    
    def __init__(self,name ,dept):
        self.name = name
        self.dept = dept
        
    
    
    def description(self):
        print(f"Name: {self.name}, Department: {self.dept}")
    


std1 = Student("Zihad",'EEE')
std2 = Student("Asraf", "CSE")
std3 = Student("Sumaiya", "Economics")

del std2.dept 
std2.description()