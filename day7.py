# Day 7: Arrays

#!/bin/python

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(raw_input())
    s = raw_input().rstrip().split()
    # s.reverse() could also be used
    print(" ".join(s[::-1]))
