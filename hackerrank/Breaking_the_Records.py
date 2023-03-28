#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    bmc = scores[0];
    blc = scores[0];
    m_count = 0;
    l_count = 0;

    for score in scores[1:]:
        if bmc < score:
            bmc = score
            m_count += 1
        elif blc > score:
            blc = score
            l_count += 1

    return m_count, l_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
