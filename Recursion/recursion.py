# @Time : 1/13/2022 3:56 PM
# @Author : klenq
# @File : recursion.py
# @Software : PyCharm

def sum(x):
    if len(x) == 0:
        return 0
    else:
        return x[0] + sum(x[1:])


def count(x):
    if len(x) == 0:
        return 0
    return 1 + count(x[1:])


def find_max(x):
    if len(x) == 0:
        return 0

    next = find_max(x[1:])
    if x[0] > next:
        return x[0]
    else:
        return next


def binary_search(x, target):
    # binary_search with recursion
    # have problems
    left = 0
    right = len(x)-1
    if right == 0:
        return None
    mid = (left + right) // 2
    if x[mid] > target:
        return binary_search(x[:mid - 1], target)
    elif x[mid] < target:
        return binary_search(x[mid + 1:], target)
    else:
        return mid


x = [2, 4, 6, 10]

print(sum(x))
print(count(x))
print(find_max(x))
print(binary_search(x, 6))
