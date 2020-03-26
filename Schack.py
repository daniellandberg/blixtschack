# Program to demonstrate
# timer objects in python

import threading as th
import time
import sys


minuter = input("hur många minuter var? ")

flag = 0
white = 60 * int(minuter)
black = 60 * int(minuter)


def toTime(tid):
    t = tid
    min = 0
    while True:
        if ((t-60) >= 0):
            min = min + 1
            t = t - 60
        if ((t-60) < 0):
            break
        sec = int(t % 60)
        if sec <= 9:
            sec = "0" + str(sec)
    return str(min) + ":" + str(sec)


def change():
    global flag
    input()
    flag = (flag + 1) % 2
    th.Thread(target=change, args=(),
              name='change', daemon=True).start()


th.Thread(target=change, args=(),
          name='change', daemon=True).start()

while True:

    # if a == '':
    #    flag = (flag + 1) % 2
    if (flag == 0):
        white -= 1
        print("vit: " + toTime(white))
    if (flag == 1):
        black -= 1
        print("Svart: " + toTime(black))
    time.sleep(1)

    if (white == 0):
        print("White loses" + "\n" + "black: " +
              str(black) + "\n" + "White: " + str(white))
        break
