# احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲
def prime_number(arg):
    primenumberlist = [2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 29, 31]
    othernumber = []
    for i in arg:
        for j in primenumberlist:
            if (i / j in arg) and (not(i == j)):
                othernumber.append(i)
    for j in othernumber:
        if j in arg:
            arg.remove(j)
    return arg


tons = list(range(1000))
print(prime_number(tons))
input()

#import numpy as np
#a=np.arange(1,1001)
