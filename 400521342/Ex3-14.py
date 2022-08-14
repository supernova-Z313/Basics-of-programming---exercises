#احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲
import time 

while True:
    nummax = int(input("please enter the max of steps "))
    n1 = 3
    pi = 4
    Rpi = input("please enter the number you want found")
    steps = 0
    start = time.process_time()
    for i in range(nummax):
        if (i % 2) == 0:
            pi = pi - (4/n1)
            n1 += 2
            print(pi)
            steps += 1
            pii =  str(pi)
            if pii[0:len(Rpi)] == Rpi:
                print(f"in step {steps} \n  \n")
                break
        else:
            pi = pi + (4/n1)
            n1 += 2
            print(pi)
            steps += 1
            pii =  str(pi)
            if pii[0:len(Rpi)] == Rpi:
                print(f"in step {steps} \n \n")
                break
    end = time.process_time()
    print("time is ", (end - start))

#3.14 =118
#3.141 = 1687
#3.14159 =136120
            