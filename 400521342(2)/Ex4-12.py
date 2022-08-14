# احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲
# توضیحات در فایل ورد
import time
import random


def Tortoise(position):
    move_type = random.randint(1, 10)
    if 1 <= move_type <= 5:
        position += 3
        return position
    elif 6 <= move_type <= 7:
        position -= 6
        if position <= 0:
            position = 1
            return position
        return position
    else:
        position += 1
        return position


def Hare(position):
    move_type = random.randint(1, 10)
    if 1 <= move_type <= 2:
        return position
    elif 3 <= move_type <= 4:
        position += 9
        return position
    elif move_type == 5:
        position -= 12
        if position <= 0:
            position = 1
            return position
        else:
            return position
    elif 6 <= move_type <= 8:
        position += 1
        return position
    else:
        position -= 2
        if position <= 0:
            position = 1
            return position
        else:
            return position


Hare_position = 1
Tortoise_position = 1
print("BANG !!!!! \nAND THEY'RE OFF !!!!!")
print("END", "-"*70, "START")
while not((Hare_position >= 70) or (Tortoise_position >= 70)):
    time.sleep(1)
    Hare_position = Hare(Hare_position)
    Tortoise_position = Tortoise(Tortoise_position)
    if Hare_position == Tortoise_position:
        print("-"*(70-Hare_position), "OUCH!!!", "-"*(Hare_position-1), end="\t\t")
        print(f"H = {Hare_position:<2} , T = {Tortoise_position:<2}")
    else:
        if Hare_position > Tortoise_position:
            print("-"*(70-Hare_position), "🐇", "-"*(Hare_position-Tortoise_position-1), "🐢", "-"*(Tortoise_position-1), end="\t \t")
            print(f"H = {Hare_position:<2} , T = {Tortoise_position:<2}")
        else:
            print("-"*(70-Tortoise_position), "🐢", "-"*(Tortoise_position-Hare_position-1), "🐇", "-"*(Hare_position-1), end="\t \t")
            print(f"H = {Hare_position:<2} , T = {Tortoise_position:<2}")
if Hare_position == Tortoise_position:
    print("It's a tie")
else:
    if Hare_position >= 70:
        print("Hare wins. Yuch.")
    else:
        print("TORTOISE WINS!!! YAY!!!")
