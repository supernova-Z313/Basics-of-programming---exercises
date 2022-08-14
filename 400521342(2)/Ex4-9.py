# احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲
def fahrenheit(C):
    fahrenheit_deg = 9 / 5 * C + 32
    fahrenheit_deg = round(fahrenheit_deg, 1)
    return fahrenheit_deg


for C in range(0, 101):
    print(fahrenheit(C))
