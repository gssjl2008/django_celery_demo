# encoding: utf-8
#@author: wuxing
#@file: sort_methods.py
#@time: 2020/4/17 10:47
#@desc:

import random
from functools import wraps
import sys

def get_data(n=20):
    return [random.randint(1,100) for i in range(n)]

# def info()


def bubble_sort(data):
    '''
    比较两两位置，小的则往前移动，时间复杂度最好O(n), 最坏O(n**2), 空间复杂度 O(1), 原地排序，属于稳定排序， 大小相同的数则位置没有改变。
    :param data:
    :return:
    '''
    print(f"{sys._getframe().f_code.co_name} init data: {data}")
    length = len(data)
    if length == 1:
        return data

    for i in range(1, length):
        for j in range(length - i):
            if data[j] > data[j+1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    print(f"{sys._getframe().f_code.co_name} result data: {data}")
    return data

def select_sort(data):
    '''
    选择排序， 从数据中选出最大值或最小值，放到首位，然后从剩余的数组中选出最大或最小值，放在第二次排序的首位
    时间复杂度最好和最坏都是 O(n**2)， 空间复杂度O(1)， 原地排序， 不稳定 ，例如： 5 8 5 2 9 --- 5 会和 2 进行交换，则第 1 个5 和 第二个 5 的位置则放生变换。
    :param data:
    :return:
    '''
    print(f"{sys._getframe().f_code.co_name} init data: {data}")
    length = len(data)
    if length == 1:
        return data

    for i in range(length):
        Min = i
        for j in range(i + 1, length):
            if data[Min] > data[j]:
                Min = j
        # if i != Min:
        data[i], data[Min] = data[Min], data[i]

    print(f"{sys._getframe().f_code.co_name} result data: {data}")
    return data


def insert_sort(data):
    '''
    将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
    从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
    （如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
    时间复杂度最好O(n),最坏O(n**2), 空间复杂度O(1)，圆度排序， 稳定排序
    :param data:
    :return:
    '''
    print(f"{sys._getframe().f_code.co_name} init data: {data}")
    length = len(data)
    if length == 1:
        return data

    for i in range(length):
        init = i - 1
        curr = data[i]                              # 必须，要不然后面直接 data[i]，值会发生改变。
        while init >= 0 and data[init] > curr:
            data[init + 1] = data[init]
            init -= 1
        data[init + 1] = curr

    print(f"{sys._getframe().f_code.co_name} result data: {data}")
    return data


def quick_sort(data):
    '''
    快速排序: 使用分治思想， 选区一个值，比他小的放于left， 其他的放于right， 递归调用，直至left和right只剩下一个元素，
    时间复杂度最好O(nlogn)，最坏O(n**2)，空间复杂度O(logn)，原地排序， 不稳定
    :param data:
    :return:
    '''

    def _quick_sort(data):
        if len(data) <= 1:
            return data

        mid = data[len(data) // 2]
        left, right = [], []
        data.remove(mid)
        for i in data:
            if i < mid: left.append(i)
            else: right.append(i)

        return _quick_sort(left) + [mid] + _quick_sort(right)



    print(f"{sys._getframe().f_code.co_name} init data: {data}")
    length = len(data)
    if length == 1:
        return data

    data = _quick_sort(data)

    print(f"{sys._getframe().f_code.co_name} result data: {data}")
    return data




if __name__ == '__main__':
    # bubble_sort(get_data())
    # select_sort(get_data())
    # insert_sort(get_data())
    quick_sort(get_data())