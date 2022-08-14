#احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲

money = 1000
years = 31
sal = 1
for i in range(1,years):
    s = money*7/100
    money +=s
    print("sod sal {0:<2} , barabar {1:<6.4} ".format(sal,s))
    print(f"megdar kol {money:<4.4}")
    sal +=1
    print("--------------------------------------------------")
