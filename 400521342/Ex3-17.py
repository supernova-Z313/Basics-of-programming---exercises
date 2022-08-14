#احمدرضا ذبیحی                       به نام خدا                 ش.د: ۴۰۰۵۲۱۳۴۲

###################################################################
# original answer                                                 #
# for i in range(1,5):                                            #
#     if i == 1:                                                  #
#        if (i % 4) == 1:                                         #
#           for j in range(1, 11):                                #
#               for z in range(1, 11):                            #
#                   if z <= j:                                    #
#                       print("*", end="")                        #
#               print()                                           #
#     if i == 2:                                                  #
#           for j in range(10, 0, -1):                            #
#               for z in range(10, 0, -1):                        #
#                   if z <= j:                                    #
#                       print("*", end="")                        #
#               print()                                           #
#     if i == 3:                                                  #
#           for j in range(10, 0, -1):                            #
#               for z in range(10, 0, -1):                        #
#                   if j < z:                                     #
#                       print(" ", end='')                        #
#                   if z <= j:                                    #
#                       print("*", end='')                        #
#               print()                                           #
#     if i == 4:                                                  #
#         print("(d)")                                            #
#         for j in range(10,0,-1):                                #
#             for z in range(1,11):                               #
#                 if z < j:                                       #
#                     print(" ",end='')                           #
#                 if z >= j:                                      #
#                     print("*",end='')                           #
#             print()                                             #
#     print("\n##########\n")                                     #
###################################################################

# answer two (this is beautiful)
while True:
    door = int(input("please enter the number of shape you want "))
    for i in range(1, door):
        if (i % 4) == 1:
            for j in range(1, 11):
                for z in range(1, 11):
                    if z <= j:
                        print("*", end="")
                print()
        if (i % 4) == 0:
            for j in range(10, 0, -1):
                for z in range(10, 0, -1):
                    if z <= j:
                        print("*", end="")
                print()
        if (i % 4) == 2:
            for j in range(10, 0, -1):
                for z in range(10, 0, -1):
                    if j < z:
                        print(" ", end='')
                    if z <= j:
                        print("*", end='')
                print()
        if (i % 4) == 3:
            for j in range(10, 0, -1):
                for z in range(1, 11):
                    if z < j:
                        print(" ", end='')
                    if z >= j:
                        print("*", end='')
                print()
