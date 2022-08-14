#احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲

check = int(input("please enter a number to check numbers before that ")) + 1
list1 = []
for i in range(1, check):
    big = i**2
    for j in range(1, check):
        side1 = j**2
        for z in range(1, check):
            side2 = z**2
            if big == (side2 + side1):
                side1_2 = str(j)
                side2_2 = str(z)
                sum_side = side1_2 + "," + side2_2
                sum_side2 = side2_2 + "," + side1_2
                if not(sum_side2 in list1):
                    list1.append(sum_side)
                    print("hypotenuse is ", i, "side one is ", j, "side two is ", z)
