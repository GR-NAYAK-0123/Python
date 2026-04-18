
"""
(i) Instance Methods

→ The methods which are defined inside a class and work with instance (object) variables are known as instance methods.

→ Instance methods must have self as the first parameter, which represents the current object.

→ We can access instance methods by using object reference only.

→ Instance methods can access:

Instance variables
Class variables

→ Instance methods are used to perform operations related to object-specific data.

→ If instance variable and local variable have same name, priority will be given to local variable.


(ii) Class Methods

→ The methods which are defined using @classmethod decorator are known as class methods.

→ Class methods take cls as the first parameter, which represents the class.

→ Class methods are used to access and modify class variables.

→ We can access class methods in 2 ways:

By using class name
By using object

→ Class methods cannot directly access instance variables.

→ If we change class variable using class method, it will reflect to all objects.


(iii) Static Methods

→ The methods which are defined using @staticmethod decorator are known as static methods.

→ Static methods do not take self or cls as parameters.

→ Static methods are used for utility or helper functions.

→ They do not access instance variables or class variables directly.

→ We can access static methods in 2 ways:

By using class name
By using object

→ Static methods are independent of object and class data.
"""
class Human:
    # This class variable
    religion = "Hindu"        # I can access this variable by using class as well as object

    def __init__(self, name, age):
        self.name = name          # These are instance variable
        self.age = age
    
    def details(self):            # This is instance method
        print(f"{self.name} {self.age}")


person1 = Human("Raja", 24)
# print(person1.religion)
# person1.religion = "xyz"

person2 = Human("Elon", 51)


Human.religion = "pqr"
print(person1.religion)
print(person2.religion)


# print(Human.religion)
# print(person1.religion)
# person1.details()
