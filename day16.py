# Day 16: Exceptions String to Integer

#!/bin/python3

import sys

s = input().strip()

try:
    print(int(s))
except:
    print('Bad String')
