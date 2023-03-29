#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(numbers):
    if len(numbers) < 2:
        return "Invalid input: list must have at least 2 elements."

    num_count = {}
    for num in numbers:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    max_frequency = 1
    min_number = float('inf')

    for num, count in num_count.items():
        if count > max_frequency:
            max_frequency = count
            min_number = num
        elif count == max_frequency:
            min_number = min(min_number, num)

    if max_frequency == 1:
        return "No duplicates found."
    else:
        return min_number


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
