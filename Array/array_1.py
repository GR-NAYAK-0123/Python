
# Here I am going to create an integer array with both posive and negative value
# And I will print those values by using any kind of loop

from array import *

arr1 = array("i", [1, 4, 8, -2, 3, 6, -10])

for value in arr1 :
    if value < 0 :
        continue

    print(value)

print("Operation Done :) ") 