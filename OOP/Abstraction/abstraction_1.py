
"""
    Abstraction :-
  ----------------
 -> Basically abstraction means hidding unneccessary details from the user and showing only neccessary details to the user
 -> And In python if we want to achieve abstraction then we have to use a library  [from abc import ABC, abstractmethod]
 
   Abstract class and method :-
 -------------------------------
 -> Abstract class is the class which have atleast one abstract method 
 -> And for creating a abstract class we have inherit that (ABC)
 -> An Abstract method doesn't have any method body, it is just a declaration but if the class want to inherit the abstract class the 
    he need to provides the implementation for the abstract method
    => And for creating an abstract method we need to use a decorator called [@abstractmethod]

"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass


class Dog(Animal):
    def eat(self):
        print("Dog is eating")

class Bird(Animal):
    def eat(self):
        print("Bird is eating")

b1 = Bird()


d1 = Dog()
d1.eat()