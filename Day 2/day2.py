import functools
input = [3, 2, 1]


def product_except_self(arr):

    zero_count = arr.count(0)
    product_without_zeros = functools.reduce(
        lambda a, b: a * b, [i for i in arr if i != 0])

    # edge case (more than one zero) -> all results will be 0
    if zero_count > 1:
        return [0] * len(arr)
    if zero_count == 1:
        return [product_without_zeros if i == 0 else 0 for i in arr]
    return [product_without_zeros / i for i in arr]

    
