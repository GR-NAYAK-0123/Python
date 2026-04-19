
class Animal:
    __name = "Lion"

    def __init__(self, age):
        self.age = age
    
    def show(self):
        print(self.age, self.__name)
    
    @classmethod
    def modify_name(cls, newName):
        cls.__name = newName
    

obj1 = Animal(21)
obj1.show()

Animal.modify_name("Tiger")

obj1.show()