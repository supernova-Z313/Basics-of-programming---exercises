# احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲

import random

def barabri(student_answer, answer):
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

def sum(number_one, number_two):
    answer = number_one + number_two
    student_answer = int(input("how much is {}+{}? (for select type of problems enter -90): ".format(number_one, number_two)))
    if student_answer == -90:
        return "go out"
    barabri(student_answer, answer)


def Submission(number_one, number_two):
    answer = number_one - number_two
    student_answer = int(input("how much is {}-{}? (for select type of problems enter -90): ".format(number_one, number_two)))
    if student_answer == -90:
        return "go out"
    barabri(student_answer, answer)


def Multiplication(number_one, number_two):
    answer = number_one * number_two
    student_answer = int(input("how much is {}*{}? (for select type of problems enter -90): ".format(number_one, number_two)))
    if student_answer == -90:
        return "go out"
    barabri(student_answer, answer)


def Division(number_one, number_two):
    if number_two == 0:
        number_two = random.randint(1, 9)
    answer = ((float(number_one / number_two))//0.01)/100
    student_answer = ((float(input("how much is {}/{}? (If the answer was a floating number, calculate it to 2 decimal places.)(for select type of problems enter -90): ".format(number_one, number_two))))//0.01)/100
    if student_answer == -90:
        return "go out"
    barabri(student_answer, answer)


while True:
    level = int(input("enter a difficulty level (1 or 2)\n(1:Questions of one-digit numbers , 2:Questions of two-digit numbers)(for exit enter -1): "))
    if level == -1:
        break
    elif level == 1:
        start = 0
        end = 9
    else:
        start = 10
        end = 99
    while True:
        challenge_type = int(input("Choose an arithmetic problem(1,2,3,4 or 5)\n(1:addition problems only , 2:subtraction problems only , 3:multiplication problems only , 4: division problems only , 5:random mixture of all these types.)\n(for select level enter -1): "))
        if challenge_type == -1:
            break
        while True:
            number_one = random.randint(start, end)
            number_two = random.randint(start, end)
            if challenge_type == 1:
                run = sum(number_one, number_two)
                if run == "go out":
                    break
            elif challenge_type == 2:
                run = Submission(number_one, number_two)
                if run == "go out":
                    break
            elif challenge_type == 3:
                run = Multiplication(number_one, number_two)
                if run == "go out":
                    break
            elif challenge_type == 4:
                run = Division(number_one, number_two)
                if run == "go out":
                    break
            else:
                functions = [sum, Submission, Division, Multiplication]
                x = random.choice(functions)(number_one, number_two)
                if x == "go out":
                    break
