#!/bin/python3

import math
import os
import random
import re
import sys


def jimOrders(orders):
    result = ""
    li1 = [];
    li_sort = []
    for num in range(len(orders)):
        li1.append(sum(orders[num]))
        li_sort.append(sum(orders[num]))
    li_sort.sort()
    for n in li_sort:
        result += str(li1.index(n) + 1)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    # print(orders)
    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
