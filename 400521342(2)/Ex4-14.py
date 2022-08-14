# احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲
import random
while True:
    number_one = random.randint(0, 9)
    number_two = random.randint(0, 9)
    student_answer = int(input(f"how much is {number_one} times {number_two}? "))
    answer = number_two * number_one
    while answer != student_answer:
        student_answer = int(input("No. Please try again. "))
    print("very good!")
