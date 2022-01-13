# @Time : 1/8/2022 11:30 AM
# @Author : klenq
# @File : Selection.py
# @Software : PyCharm

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr


print(selection_sort([5, 4, 3, 2, 1, 19, 12]))
