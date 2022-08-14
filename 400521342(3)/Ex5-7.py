# احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲
def list_unique(arg):
    for i in arg:
        while arg.count(i) >= 2:
            arg.remove(i)
    return arg

arg = [1, 2, 2, 3, 12, 12, 12, 12, 4, 8,8,6]
d = list_unique(arg)
print(sorted(d))

input()
