# Day 29: Regex, patterns and intro to DBs

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())
    gmailIDs = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if "@gmail.com" in emailID:
            gmailIDs.append(firstName)

    gmailIDs.sort()
    for i in range(len(gmailIDs)):
        print(gmailIDs[i])
