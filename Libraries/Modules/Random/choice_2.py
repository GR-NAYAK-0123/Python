
""" from -> It means we can import a specific function from a module, So at the time of calling that function
            we don't need to use that module name associated with the function
"""

from random import choice

coin = choice(['Heads', 'Tails'])
print(coin)