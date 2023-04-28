import itertools


def sumnums(lst, k):
    for num in lst:
        for num2 in lst:
            if num + num2 == k:
                return True
    return False


#print(sumnums([10, 15, 3, 7], 17))

def sumnums2(lst, k):
    for num in lst:
        if k - num in lst:
            return True
    return False


#print(sumnums2([10, 15, 3, 7], 17))

def sumnums3(lst, k):
    return any(k - num in lst for num in lst)


print(sumnums3([10, 15, 3, 7], 17))

# Bonus: Can you do this in one pass?


def sumnums4(lst, k):
    seen = set()
    for num in lst:
        if k - num in seen:
            return True
        seen.add(num)
    return False


print(sumnums4([10, 15, 3, 7], 17))


def sumnums5(lst, k):
    return any(k - num in lst[:i] for i, num in enumerate(lst))


print(sumnums5([10, 15, 3, 7], 17))


def sumnums6(lst, k):
    for num in range(len(lst)):
        for num2 in range(len(lst)):
            if num != num2 and lst[num] + lst[num2] == k:
                return True

    return False


print(sumnums6([10, 15, 3, 7], 17), "5")
print(sumnums6([11, 1, 2, 5], 17), "5")

