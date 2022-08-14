#احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲

total_gallons = 0
total_miles = 0
while True:
    a = int(input("Enter the gallons used (-1 to end): "))
    if a == -1:
        break
    b = int(input("Enter the miles driven: "))
    print("The miles/gallon for this tank was {}".format(b/a))
    total_gallons += a
    total_miles += b
print(f"The overall average miles/gallon was {total_miles/total_gallons}")
