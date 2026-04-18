
class Human:

    # This is kind of a constructor and inside this all the variables are instance variable
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # This is called instance method, we can access this method by using object only
    def details(self):
        print(f"The person {self.name} age is {self.age}")

person1 = Human("Raja", 24)

# print(person1.name)
# print(person1.age)
# person1.age = 23
# print(person1.age)

person1.details()

# person2 = Human(20)   # Here We can't create an object by passing only one argument
# person2.details()