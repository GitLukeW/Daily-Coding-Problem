import functools


def product(accumulated_array, next_value):
    accumulated_array.append(accumulated_array[-1] * next_value)
    return accumulated_array


def main(input):
    result = functools.reduce(product, input, [1])
    result.pop()

    running_product_from_right = 1
    for i in range(1, len(result) + 1):
        result[-i] = result[-i] * running_product_from_right
        running_product_from_right = running_product_from_right * input[-i]
        return result


# tests
print(main([5, 1, 4, 3, 6]) == [72, 360, 90, 120, 60])
# with one zero (all but the zero will be 0)
print(main([5, 1, 0, 3, 6]) == [0, 0, 90, 0, 0])
# with multiple zeros (all will be 0)
print(main([100, 0, 1, 3, 9, 0, 55]) == [0, 0, 0, 0, 0, 0, 0])
