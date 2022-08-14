# احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲
def tuple_maker(a, b, c):
    list_one = []
    list_one.append(c)
    list_one.append(a)
    list_one.append(b)
    return tuple(list_one)
a, b, c = 'doug', 22, 1984
a, b, c = tuple_maker(a, b, c)
print(a, b, c)

a, b, c = tuple_maker(a, b, c)
print(a, b, c)

a, b, c = tuple_maker(a, b, c)
print(a, b, c)
