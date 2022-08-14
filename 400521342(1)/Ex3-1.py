#احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲

passes = 0
fail = 0
b = ["1","2"]
for st in range(10):
    result = input('Enter result (1=pass, 2=fail): ')
    while not(result in b):
        print("input is incorrect")
        result = input('Enter result (1=pass, 2=fail): ')
    if int(result) == 1:
        passes +=1
    else:
        fail +=1
print('Passed:', passes)
print('Failed:', fail)

if passes > 8:
    print("Bonus to instructor")
