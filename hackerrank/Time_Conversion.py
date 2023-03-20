#!/bin/python3

import math
import os
import random
import re
import sys
import time
from datetime import datetime


def timeConversion(Time):
    timestamp = time.mktime(datetime.strptime(Time, "%I:%M:%S%p").timetuple())

    return datetime.fromtimestamp(timestamp).strftime("%H:%M:%S")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
