#احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲

while True:
    nummax = int(input("please enter the max of steps "))
    n1 = 2
    e = 1
    n2 = 1
    for i in range(nummax):
        e = e + (1/n2)
        n1 += 1
        print(e)
        n2 = 1
        for i in range(1,n1):
            n2 *= i
