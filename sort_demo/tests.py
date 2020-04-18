from django.test import TestCase

# Create your tests here.


# 冒泡排序

import random
from functools import wraps

def get_data(n=20):
    return [random.randint(1,100) for i in range(n)]

def show(func):
    @wraps(func)
    def _inner(data):
        print(f"data: {data}")
        tmp = data
        print(f"tmp:{tmp}")
        result = func(data)
        print(f"result: {result}")
        if sorted(tmp) == result:
            print("result: True")
        else:
            print(f"sorted: {sorted(tmp)}")
        return result
    return _inner


def bubble_sort(data):
    print(f"data: {data}")
    length = len(data)
    if length <= 1:
        return data

    while length > 0:
        for i in range(length - 1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
        length -= 1
    
    print(f"result: {data}")


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


if __name__ == '__main__':
    data = get_data()
    # data = [1,5,4,3,2]
    quick_sort(data)