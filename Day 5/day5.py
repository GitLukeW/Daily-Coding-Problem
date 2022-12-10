

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    return pair(lambda a, b: a)


def cdr(pair):
    return pair(lambda a, b: b)

# car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.


print(car(cons(3, 4)) == 3)
print(cdr(cons(3, 4)) == 4)
