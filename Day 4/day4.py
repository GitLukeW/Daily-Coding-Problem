
def main(arr):
    # put all negatives at the front (I had to look this approach up..)
    negative_count = 0
    for i in range(len(arr)):
        if arr[i] <= 0:
            arr[negative_count], arr[i] = arr[i], arr[negative_count]
            negative_count += 1

    # if they are all negative, 1 is missing
    if negative_count == len(arr):
        return 1

    # mark each index that is present as negative
    # (but it's slightly complicated because you're starting after the negative numbers that you already put at the front)
    # so you need to add that to the value (and subtract one, because arrays are zero indexed, but the first integer you care about is 1)
    for i in range(negative_count, len(arr)):
        val = abs(arr[i])
        index_for_value = val + negative_count - 1
        if index_for_value < len(arr):
            arr[index_for_value] = -arr[index_for_value]

    # print the index of the first value in the once positive half of the array that was not marked as negative to denote presence:
    for i in range(negative_count, len(arr)):
        if arr[i] > 0:
            return i + 1 - negative_count

    return len(arr) + 1

# find the first missing positive int in
# O(n) time (linear time) ### AKA no sorting, because most efficient sorting algos are n(log(n))  - slightly worst than n
# O(1) space (constant space) ### AKA no additional complex storage (no more arrays or hashes that vary with input size)


# tests
print(main([3, 4, -1, 1]) == 2)
# [3, 4, -1, 1]
print(main([-5, 1, 6, 2, 1000, 5, 3]) == 5)
print(main([-5, 1, 6, 2, -1000, 5, -3]) == 3)
print(main([-5, -1, -6, -2, -1000, -5, -3]) == 1)  # all negative
print(main([5, 4, 3, 2, 1]) == 6)  # all present
