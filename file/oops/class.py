#class 
class car:
    def __init__(self,brand,color):
        self.brand= brand   #Attribute
        self.color= color   #Attribute
    def drive(self):    #Method
        print(f"{self.color} {self.brand} is driving🚗")
        
#object 
car1=car("BMW",'Black')
car2=car("Tesla",'White')
car1.drive()
car2.drive()

#constructor: __init__  is a constructor which is called when an object
# of the class is created.