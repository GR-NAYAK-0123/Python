
import random

unknownNumber = random.randint(1, 10)

count = 0

while True:
    guessNumber = int(input("Guess the number between 1 and 10 : "))
    count += 1
    if guessNumber == unknownNumber:
        print("Congradulations you are correct :)")
        print(f"You took {count} chance to guess the correct number")
        break
    else:
        print("You are very close ! Try again ):")

