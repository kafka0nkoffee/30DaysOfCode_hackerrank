# Day 5: Loops

#!/bin/python

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1, 11):
        product = n * i
        print("{} x {} = {}".format(n, i, product))
