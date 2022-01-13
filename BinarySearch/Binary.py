print('Binary Search')


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        index = (low + high) // 2
        if arr[index] < target:
            low = index + 1
        elif arr[index] > target:
            high = index - 1
        else:
            return index

    return None


my_list = [1, 3, 5, 6, 7, 8, 9, 19]

print(binary_search(my_list, 5))
