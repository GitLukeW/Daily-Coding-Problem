list = [10, 15, 3, 7]
k = 17


def add_nums(list, k):
    for x in list:
        for y in list:
            if x + y == k:
                return True


print(add_nums(list, k))
