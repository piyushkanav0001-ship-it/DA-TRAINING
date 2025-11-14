self.age = age

    def greet(self):
        print(f"My name is {self.name} and I am {self.age} years old")
result=Person("Yash",18) 
result.greet()



class Calculator:"""
"""def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid choice")

# Run the calculator
calculator()"""

"""#class
class car:
    def _init_(self,brand,color):
        self.brand=brand #attribute
        self.color=color #attribute

    def drive(self): #mentioned
        print(f"{self.color}{self.brand}is driving 🚗")
#object
car1=car("bmw","black")
car2=car("tesla","white")

car1.drive()
car2.drive()"""

"""class bankaccount:
    def _init_(self,balance):
        self.__balance+=amount
    def deposite(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
account = bankaccount(1000)
account.deposite(500)
print(account.get_balance())#1500
        
class car:
    def _init_(self,brand,color):
        self.brand=brand #attribute
        self.__color=color #attribute

    def drive(self): #mentioned
        print(f"{self.__color}{self.brand}is driving 🚗")
#object
car1=car("bmw","black")

print(car1.brand)
print(car1.__color)
car1.drive()

class animal:
    def speak(self):
        print("animal speaks")
class Dog(animal):
    def speak(self):
        print("Dog breaks")
dog=Dog()  
dog.speak()


class Person:
    def _init_(self, name, age):
        self.name=name
        self.__age=age
    p1=Person("Email",25)
    print(p1.name)
    print(p1.Person__age)   

class Cat:
    def sound(self):
        return"Meow"
class Dog:
    def sound(self):
        return"Woof
class Animal:
    def speak(self):
        print("Animals make differentsound")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat meows")
for pet in (Dog(),Cat()):
    pet.speak()     """                   
     
       
import pandas as pd

data=[10,20,30]
s=pd.Series(data)
print(s)
       
data= {
    'name':['ritik','aman','priya'],
    'age':[21,23,34],
    'marks':[23,45,78]
}    

df = pd.DataFrame(data)
print(df)

Data=[34,67,89]
y=pd.Series(Data)
print(y)

a=[1,2,3,]
myvar=pd.Series(a,index=['x','y','z'])
print(myvar["y"])
print(myvar)


calories={"day1":420,"day2":380,"day3":390}
myvar=pd.Series(calories)
print(myvar)

marks={"math":89,"science":45,"sst":67}
e=pd.Series(marks)
print(e)
print(e[1])
De
