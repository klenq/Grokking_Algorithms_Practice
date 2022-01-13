# @Time : 1/13/2022 5:37 PM
# @Author : klenq
# @File : quick_sort.py
# @Software : PyCharm

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        # O(n^2) for choosing first element as pivot
        # O(nlogn) for choosing random element as pivot
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


