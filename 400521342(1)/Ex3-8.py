#احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲

num1 = int(input("please enter your first number "))
num2 = int(input("please enter your second number "))
num3 = int(input("please enter your third number "))
num4 = int(input("please enter your fourth number "))
print("sum of number is %d"%(num1+num2+num3+num4))
print("average of number is {}".format((num1+num2+num3+num4)/4))
print('product of number is {0}'.format(num1*num2*num3*num4))

#way 1
#b = [num1,num2,num3,num4]
#c = sorted(b)
#print(f"min = {c[0]}")
#print(f"max = {c[3]}")
#way 2
#c = [num1,num2,num3,num4]
#print(min(c))
#print(max(c))

cx = [num3 , num4, num2]
bozorg = num1
kochik = num1
for i in cx:
    if bozorg <= i:
        bozorg = i
    #-----------------
    if kochik >= i:
        kochik = i
        
print("max = ",bozorg)
print("min = ", kochik)
