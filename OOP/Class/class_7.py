
class Human:
    religion = "Hindu"

    def __init__(self, name):
        self.name = name
    
    @classmethod
    def class_method(cls):
        cls.religion = "xyz"

    @staticmethod
    def static_method():
        print("Good Evening")
    
    # This is a normal method inside the class and we can only access this method with the help of class
    def greet():
        print("Good Night :)")

obj1 = Human("Raja")

# obj1.static_method()

#obj1.class_method()
#print(obj1.religion)

# Human.class_method()
# print(obj1.religion)

Human.greet()
obj1.greet()

