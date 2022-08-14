#احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲

line = 1
while True:
    for j in range(1, 11):
        if line == j:
            for z in range(1, 11):
                if z <= j:
                    print("*", end="")
                if z > j:
                    print(" ", end="")
    print("   ", end="")
    for j in range(1, 11):
        if line == j:
            for z in range(10, 0, -1):
                if z >= j:
                    print("*", end="")
                if z < j:
                    print(" ", end="")
    print("   ", end="")
    for j in range(1, 11):
        if line == j:
            for z in range(1, 11):
                if z < j:
                    print(" ", end='')
                if z >= j:
                    print("*", end='')
    print("   ", end="")
    for j in range(1, 11):
        if line == j:
            for z in range(10, 0, -1):
                if z > j:
                    print(" ", end='')
                if z <= j:
                    print("*", end="")
    print()
    if line == 10:
        break
    line += 1
