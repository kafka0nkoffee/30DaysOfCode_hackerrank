# Day 11: 2D Arrays

#!/bin/python

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    arr = []
    largestSum = []
    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    for i in range(0, 4):
        for j in range(0, 4):
            sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j +
                                                                         1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            largestSum.append(sum)

    final = sorted(largestSum)
    print(final[15])
