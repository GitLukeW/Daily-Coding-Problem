import itertools

list = [10, 15, 3, 7]
k = 17


def add_nums(list, k):
    for x in list:
        for y in list:
            if x + y == k and x != y:
                return True


print(add_nums(list, k))


def iter(list, k):
    for x in itertools.combinations(list, 2):
        print(x)
        if sum(x) == k:
            return True


print(iter(list, k))
