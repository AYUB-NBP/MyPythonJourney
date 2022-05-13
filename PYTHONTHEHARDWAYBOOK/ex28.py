# Quizz: True or False

def Quizz_format(b1, op, b2):
    if op == 'or':
        result = b1 or b2
        print(result)
    elif op == 'and':
        result = b1 and b2
        print(result)
    elif op == "==":
        result = b1 == b2
        print(result)
    elif op == "!=" or "not" or "Not" or "NOT":
        result = b1 != b2
        print(result)
    elif op == ">=":
        result = b1 >= b2
        print(result)
    elif op == "<=":
        result = b1 <= b2
        print(result)


a = input("Write first compared element:\n\t")
b = input("Write comparison operator:\n\t")
c = input("Write first compared element:\n\t")

type = type(a), type(b), type(c)

Quizz_format(a, b, c)
