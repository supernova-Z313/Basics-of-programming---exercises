# احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲
import random
answer = random.randint(1, 1000)
guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: (for exit enter 0) "))
count = 1
while guess != answer:
    if guess == 0:
        break
    else:
        if guess > answer:
            guess = int(input("Too high. Try again.(for exit enter 0) "))
            count += 1
        else:
            guess = int(input("Too low. Try again.(for exit enter 0) "))
            count += 1
if guess == answer:
    if count <= 10:
        print("Congratulations. You guessed the number! Either you know the secret or you got lucky!")
    else:
        print("You should be able to do better!")
