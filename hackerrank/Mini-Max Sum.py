#!/bin/python3
import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    rst = []
    for n in range(len(arr)):
        stack = arr[n]
        arr.remove(arr[n])
        rst.append(sum(arr))
        arr.insert(n, stack)

    return print(min(rst), max(rst))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
