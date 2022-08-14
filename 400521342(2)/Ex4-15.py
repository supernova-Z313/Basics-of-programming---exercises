# احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲
import random
while True:
    number_one = random.randint(0, 9)
    number_two = random.randint(0, 9)
    student_answer = int(input(f"how much is {number_one} times {number_two}? "))
    answer = number_two * number_one
    luck = random.randint(1, 3)
    while answer != student_answer:
        if luck == 1:
            student_answer = int(input('No. Keep trying.'))
        elif luck == 2:
            student_answer = int(input('Wrong. Try once more.'))
        else:
            student_answer = int(input("No. Please try again. "))
        luck = random.randint(1, 3)
    if luck == 1:
        print('Nice work!')
    elif luck == 2:
        print('Keep up the good work!')
    else:
        print("very good!")
