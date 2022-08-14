# احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲
import random
difficulty = int(input("enter a difficulty level(1 or 2): "))
if difficulty == 1:
    kaf = 0
    sagf = 9
else:
    kaf = 10
    sagf = 99
while True:
    number_one = random.randint(kaf, sagf)
    number_two = random.randint(kaf, sagf)
    student_answer = int(input(f"how much is {number_one} times {number_two}? "))
    answer = number_two * number_one
    lock = random.randint(1, 3)
    while answer != student_answer:
        if lock == 1:
            student_answer = int(input('No. Keep trying.'))
        elif lock == 2:
            student_answer = int(input('Wrong. Try once more.'))
        else:
            student_answer = int(input("No. Please try again. "))
        lock = random.randint(1, 3)
    if lock == 1:
        print('Nice work!')
    elif lock == 2:
        print('Keep up the good work!')
    else:
        print("very good!")
