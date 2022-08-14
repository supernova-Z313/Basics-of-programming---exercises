#احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲

#way1:
#number1 = int(input("please enter a 5 digit number "))
#if number1[0:2] == number1[-1:-3:-1]:
#    print("this is a palindrome number")
#else:
#   print("this is not a palindrome number")
#===========================================================
#way2:
#number1 = input("please enter a 5 digit number ")
#b = ""
#for i in number1:
#    b = str(i) + b
#if b == number1:
#    print("this is a palindrome number")
#else:
#   print("this is not a palindrome number")
#===========================================================
#way3:
number1 = int(input("please enter a 5 digit number "))
digit1 = number1//10000
digit2 = (number1%10000)//1000
digit4 = (number1%100)//10
digit5 = number1%10
if digit1 == digit5:
    if digit2 == digit4:
        print("this is a palindrome number")
    else:
        print("this is not a palindrome number")
else:
    print("this is not a palindrome number")
