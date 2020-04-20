from django.test import TestCase

# Create your tests here.


# 冒泡排序

import random
import sys
from functools import wraps

success = []

def get_data(n=20):
    return [random.randint(1,100) for i in range(n)]

def show(func):
    @wraps(func)
    def _inner(data):
        global result
        print(f"{func.__name__}, data: {data}")
        tmp = data
        print(f"{func.__name__},tmp:{tmp}")
        result = func(data)
        print(f"{func.__name__}, result: {result}")
        if sorted(tmp) == result:
            print("result: True")
            success.append(True)
        else:
            print(f"sorted: {sorted(tmp)}")
            success.append(False)
        return result
    return _inner

@show
def bubble_sort(data):
    # print(f"data: {data}")
    length = len(data)
    if length <= 1:
        return data

    while length > 0:
        for i in range(length - 1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
        length -= 1

    return data
    # print(f"result: {data}")


@show
def insert_sort(data):
    length = len(data)
    if length <= 1:
        return data

    for i in range(length):
        j = i - 1
        cur = data[i]
        while j >= 0 and data[j] > cur:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = cur

    return data

@show
def select_sort(data):
    length = len(data)
    if length <= 1:
        return data

    for i in range(length - 1):
        index = i
        for j in range(i + 1, length):
            if data[index] > data[j]:
                index = j
        data[i], data[index] = data[index], data[i]
    return data

@show
def quick_sort(data):

    def _quick_sort(data):
        if len(data) <= 1:
            return data

        mid = data[len(data) // 2]
        print(f"mid: {mid}")
        left, right = [], []
        data.remove(mid)

        for i in data:
            if i < mid: left.append(i)
            else: right.append(i)
        
        return _quick_sort(left) + [mid] + _quick_sort(right)

    result = _quick_sort(data)
    
    return result

@show
def bubble_sort2(data):
    length = len(data)
    if length <= 1:
        return data

    while length > 0:
        for i in range(length - 1):
            if data[i+1] < data[i]:
                data[i], data[i+1] = data[i+1], data[i]
        length -= 1
    return data

@show
def insert_sort2(data):
    length = len(data)
    if length <= 1:
        return data

    for i in range(1, length):
        j = i - 1
        cur = data[i]
        while j >=0 and data[j] > cur:
            data[j+1] = data[i]
            j -= 1
        data[j + 1] = cur

    return data


@show
def select_sort2(data):
    length = len(data)
    if length <= 1:
        return data

    for i in range(length - 1):
        min = i
        for j in range(i + 1, length):
            if data[j] < data[min]:
                min = j
        data[i], data[min] = data[min], data[i]


    return data

if __name__ == '__main__':

    for i in range(100):
        arr = get_data()
        arr2 = arr.copy()
        select_sort(arr)
        select_sort2(arr2)
    print(success)