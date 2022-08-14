# احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲
def product(num):
    y = 1
    for char in num:
        y *= char
    return y


number = []
door = int(input("please enter how many number you want enter: "))
for i in range(door):
    x = int(input("enter a number "))
    number.append(x)

print(product(number))
