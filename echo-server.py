import socket
import time


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


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1251))
s.listen(5)
flag = 1
Connection = []
Adresses = []
while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    Connection.append(clientsocket)
    Adresses.append(address)
    if len(Connection) == 1:
        msg = "How many minutes?"
        msg = f"{msg}"
        clientsocket.send(bytes(msg, "utf-8"))
        tid = (clientsocket.recv(1024))
        tid1 = int(tid.decode("utf-8"))*60
        tid0 = tid1
    if len(Connection) == 2:
        break
while True:
    time.sleep(1)
    print(str(flag))
    print("över")
    if int(flag) == 1:
        tid1 = tid1 - 1
        vit = toTime(tid1)
        svart = toTime(tid0)
        msg = f"{vit}, {svart}, {flag}"
        Connection[0].send(bytes(msg, "utf-8"))
        sms = f"{vit}, {svart}, {flag}"
        Connection[1].send(bytes(sms, "utf-8"))
        flag = (Connection[0].recv(1024))
        flag = str(flag.decode("utf-8"))

    else:
        tid0 = tid0 - 1
        vit = toTime(tid1)
        svart = toTime(tid0)
        msg = f"{vit}, {svart}, {flag}"
        Connection[1].send(bytes(msg, "utf-8"))
        sms = f"{vit}, {svart}, {flag}"
        Connection[0].send(bytes(sms, "utf-8"))
        flag = (Connection[1].recv(1024))
        flag = str(flag.decode("utf-8"))

    if tid1 == 0:
        flag = 4
        sms = f"{tid1}, {tid0}, {flag}"
        Connection[0].send(bytes(sms, "utf-8"))
        Connection[1].send(bytes(sms, "utf-8"))
    if tid0 == 0:
        flag = 3
        sms = f"{tid1}, {tid0}, {flag}"
        Connection[1].send(bytes(sms, "utf-8"))
        Connection[0].send(bytes(sms, "utf-8"))
