#احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲

while True:
    co1 = 1
    for i in range(10):
        number = int(input("enter the number"))
        if co1 == 1:
            a = number
            c = number
        if number >= a:
            if co1 == 1:
                b = number
            if (number > b)and(b >= c):
                c = b
                b = number
            if (number < b)and(number > c):
                c = number
            
        else:
            if co1 == 2:
                c = number
            if (number > c):#and(number < b)
                c = number
            a = number
        co1 += 1
        
    print(b," and ",c)
