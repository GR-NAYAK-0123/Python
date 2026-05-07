
class Car:
    def __init__(self, wheel, speed):
        self.wheel = wheel
        self.speed = speed
    
    def details(self):
        print(f"{self.wheel}, {self.speed}")

class Audi(Car):
    def __init__(self, wheel):
        self.wheel = wheel
    
    # # def details(self):
    #     print(self.wheel)


obj1 = Audi(4)
obj1.details()     # We will error here because Audi doesn't have any speed argument
