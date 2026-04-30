
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def display(self):
        print(self.name, self.age)


lion = Animal("lion")

print(lion.name)

obj = Dog("w", 10)
obj.display()