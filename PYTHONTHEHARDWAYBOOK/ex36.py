# The zigzag animation game
import time

list = []
s = .2


def zig():
    if len(list) < 10:
        for i in range(0, 10):
            list.append("X")
            speed(s)
            print(list)


def zag():
    while len(list) > 0:
        list.pop(0)
        speed(s)
        print(list)


def zigzag():
    x = 1
    while x == 1:
        zig()
        zag()


def speed(x):
    time.sleep(x)


zigzag()
