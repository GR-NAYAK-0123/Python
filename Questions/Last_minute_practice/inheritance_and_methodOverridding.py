
# Inheritance and method overridding

class Animal:
    def speak(self):
        print("Animal speak")

class Dog(Animal):
    def speak(self):
        print("Dog speak")

class Cat(Animal):
    def speak(self):
        print("Cat speak")

c1 = Cat()
d1 = Dog()
a1 = Animal()

c1.speak()
d1.speak()
a1.speak()