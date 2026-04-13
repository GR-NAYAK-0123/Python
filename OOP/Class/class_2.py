
class laptop:

    def details(self, brand, ram):
        print(brand, " ", ram)

# Creating an object for the class laptop
lap1 = laptop()
lap2 = laptop()

lap1.details("Dell", "16GB")
lap2.details("HP", "8GB")