#!/usr/bin/python3
for number in range(0, 10):
    for number2 in range(1, 10):
        if number < number2:
            if number == 8 and number2 == 9:
                print("{}{}".format(number, number2))
            else:
                print("{}{}".format(number, number2) , end=", ")
