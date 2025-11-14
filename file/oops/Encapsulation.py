class Person:
    def __init__(self,name, age):
        self.name=name 
        self.__age=age  #private attribute
p1= Person("AMAN",19)
print (p1.name)
       # print(f"My age is {p1._age}") will take a error bcz age is private here
print(p1._Person__age)  #this is called name mangling to access private attribute
