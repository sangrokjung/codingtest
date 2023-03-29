#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(numbers, n):
    if n <= 0:
        return "Invalid input: n must be greater than 0."

    sum_list = []
    count = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            pair_sum = numbers[i] + numbers[j]
            sum_list.append(pair_sum)
            if pair_sum % n == 0:
                count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(ar, k)

    fptr.write(str(result) + '\n')

    fptr.close()
