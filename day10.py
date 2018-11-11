# Day 10: Binary Numbers

#!/bin/python

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(raw_input())
    count = 0
    most = 0
    #bin = 0
    while n > 0:
        rem = n % 2
        if rem == 1:
            count += 1
            if count > most:
                most = count
        else:
            count = 0
        n = n / 2
        #bin = bin*10 + rem

    print most
