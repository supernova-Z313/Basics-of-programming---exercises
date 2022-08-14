# احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲

def seconds_since_midnight(hour, minute, second):
    hour_in_second = hour * 3600
    minute_in_second = minute * 60
    return hour_in_second + minute_in_second + second


hour1 = int(input("enter the hour "))
minute1 = int(input("enter the minute "))
second1 = int(input("enter the second "))
print(seconds_since_midnight(hour1, minute1, second1))
