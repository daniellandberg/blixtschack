import socket
import threading as th
import time
import sys

HEADERSIZE = 10
global flag


def change():
    global flag
    input()
    flag = 0
    print(" ")
    th.Thread(target=change, args=(),
              name='change', daemon=True).start()


host = '00.00.00.00'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, 1251))

th.Thread(target=change, args=(),
          name='change', daemon=True).start()
tid = (s.recv(1024))
tid = str(tid.decode("utf-8"))
tid = input(tid)
tid = f"{tid}"
s.send(bytes(tid, "utf-8"))
winner = 0
while True:
    flag = 1
    msg = (s.recv(1024))
    msg = str(msg.decode("utf-8"))
    msg = msg.split(",")
    if int(msg[2]) > 2:
        winner = int(msg[2])
        break
    temp = int(msg[2])
    # print(msg)
    if temp == 1:
        print("White: " + str(msg[0]) + " ---- " +
              "Black:" + str(msg[1]) + "\n")
        flag = f"{flag}"
        s.send(bytes(flag, "utf-8"))

    else:
        print("White: " + str(msg[0]) + " ---- " +
              "Black:" + str(msg[1]) + "\n")

if winner == 4:
    print("you lost!")
else:
    print("you won!")
