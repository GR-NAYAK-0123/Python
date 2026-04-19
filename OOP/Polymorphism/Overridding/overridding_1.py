
class Animal:
    def show(self):
        print("This is from Animal")

class Lion(Animal):
    # Here I override the show method
    def show(self): 
        # super().show()  
        print("This is from Lion")

obj1 = Lion()
obj1.show()