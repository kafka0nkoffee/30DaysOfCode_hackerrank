# Day 6: Let's Review

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
even = ""
odd = ""
for i in range(T):
    s = raw_input()
    for i in range(len(s)):
        if i % 2 == 0:
            even += s[i]
        else:
            odd += s[i]
    print(even + " " + odd)
    odd = ""
    even = ""
