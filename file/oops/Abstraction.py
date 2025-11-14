from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(vehicle):
    def start(self):
        print("Car Started")
class Bike(vehicle):
    def start(self):
        print("Bike Started")
vehicles = [Car(),Bike()]
for v in vehicles:  
    v.start()