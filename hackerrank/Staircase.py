#!/bin/python3

import math
import os
import random
import re
import sys


def staircase(n):
    word = "#"
    for i in range(n, 0, -1):
        print(f'{(word * (n - i + 1)).rjust(n, " ")}')


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
