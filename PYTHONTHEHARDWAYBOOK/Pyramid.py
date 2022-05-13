list = []


def list_filler():
    for i in range(1, 10):
        list.append(i)
        print(list)


def list_emptier():
    for i in range(-10, -2):
        list.pop()
        print(list)


list_filler()
list_emptier()
