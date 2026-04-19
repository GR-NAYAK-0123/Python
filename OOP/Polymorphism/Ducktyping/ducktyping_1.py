
# It means executing the respective class methods

class Animal:
    def show(self):
        print("I am from Animal")


class Human:
    def show(self):
        print("I am from Human")

obj1 = Animal()
obj2 = Human()

obj1.show()
obj2.show()