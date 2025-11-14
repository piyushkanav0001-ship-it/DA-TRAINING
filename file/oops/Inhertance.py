class animal:

  def speaks(self):
   print("Animal speaks")

class Dog(animal):    #Dog inherits animal
     def speaks(self):
      print("Dog barks 🐶")
dog=Dog()
dog.speaks()  #calling inherited method