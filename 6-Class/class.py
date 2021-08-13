class Human():
    
    def __init__(self, name, age, gender):
        self.fame = name
        self.age = age 
        self.gender = gender
        
    def info(self):
        return 'Name: ', self.fame, 'Age: ', self.age, 'Gender:', self.gender
    
    def name1(self):
        return self.fame
        

human1  = Human('Keya', 21, 'Female')
human2 = Human('Joy', 22, 'Male')

print(human1.name1())
