# Day 20: Sorting

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split()))
# Write Your Code Here

# Track number of elements swapped during a single array traversal
numberOfSwaps = 0

for i in range(n):
    for j in range(n - i - 1):
        # Swap adjacent elements if they are in decreasing order
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
            numberOfSwaps += 1

print("Array is sorted in {} swaps.".format(numberOfSwaps))
print("First Element:", a[0])
print("Last Element:", a[n - 1])
