
# Here I am going to copy one array values to another array

from array import *

arr1 = array('i', [1, 2, 3, 4, 5])

arr2 = array(arr1.typecode, (n for n in arr1)) 

for value in arr2 :
    print(value)

print(arr1.buffer_info())  # It gives the address of the array and also gives the size of the array