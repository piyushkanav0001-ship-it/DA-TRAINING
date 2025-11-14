# create class named as rectangle
# there is attributes in it a and b
# there is method named as area which return area of rectangle
# get input from user for a and b


class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth

a = float(input("Enter length: "))
b = float(input("Enter breadth: "))
area = rectangle(a, b)
print("Area of rectangle is:", area.area())