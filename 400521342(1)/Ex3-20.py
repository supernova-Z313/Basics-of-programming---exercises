#احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲

# easy way
# number = int(input("enter a number "), 2)
# print(number)

number = input("please enter a binary number (form of binary number is = 0b.... ,for example 0b1101 = 13)")
number_1 = number[::-1]
counter = 1
R_number = 0
for i in number_1:
    if i == 'b':
        print(R_number)
        break
    R_number += (counter * int(i))
    counter *= 2
