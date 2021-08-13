class Car():
    
    def __init__(self, brand, model, fueltype, milage):
        self.brand = brand
        self.model = model
        self.fueltype = fueltype
        self.milage = milage
    
    def car_description(self): 
        print("Car: " + self.brand + ", Model: " + self.model+ ", Fuel type: " + self.fueltype + ", Milage: " + self.milage)
        
person1 = Car('Tesla', 'Rodstar X', 'Electric', '12km/charge')
person2 = Car('Audi', 'A8', 'Octane', '10km/ltr')

person2.car_description()
print(dir(Car))