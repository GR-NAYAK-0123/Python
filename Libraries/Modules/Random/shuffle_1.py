
# shuffle -> It basically suffle a collection of an element like list but it doesn't return anything

import random

cards = ["King", "Queen", "Ace"]

# Before shuffle
for card in cards:
    print(card)

random.shuffle(cards)

# After shuffle
print("---------------")
for card in cards:
    print(card)