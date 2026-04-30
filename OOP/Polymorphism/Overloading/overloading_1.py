

class Animal:
    def show(self, name):
        print("I am from Animal")
    
    # In python method overloading doesn't work, It simply overriddes the previous method
    def show(self):
        print("From Animal with name ----")
    
obj1 = Animal()
obj1.show()