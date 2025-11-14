class Cat:
    def sound(self):
        return "Meow😹"
class Dog:
    def sound(self):
        return "Bark🐶"
for animal in (Cat(), Dog()):
    print(animal.sound())