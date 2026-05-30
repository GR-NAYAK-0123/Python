
# If we want to use any function of any module then first we have to import that function
""" import -> It basically import all the function inside the module
     but when you want to call any function then you have use [module.functionName] """

import random   # It means, it imports all the function inside the random module

coin = random.choice(['Head', 'Tail'])

print(coin)
