# احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲
import random
answer = random.randint(1, 1000)
guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: (for exit enter 0) "))
while guess != answer:
    if guess == 0:
        break
    else:
        if guess > answer:
            guess = int(input("Too high. Try again.(for exit enter 0) "))
        else:
            guess = int(input("Too low. Try again.(for exit enter 0) "))
if guess == answer:
    print("Congratulations. You guessed the number! ")
