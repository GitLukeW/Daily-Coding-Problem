test = [3, 4, -1, 1]
# output == 2

sorted_test = sorted(test)
print(sorted_test)

for num in sorted_test:
    check = 1
    if num != check:
        check += 1
    else:
        check += 0
print(check)
