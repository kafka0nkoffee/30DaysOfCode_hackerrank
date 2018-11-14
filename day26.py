# Day 26: Nested Logic

ac_day = input().split()
ac_day = list(map(lambda x: int(x), ac_day))
ex_day = input().split()
ex_day = list(map(lambda x: int(x), ex_day))

# [0] = day, [1] = month and [2] = year
fine = 0
if ac_day[2] <= ex_day[2]:  # year
    if ac_day[1] <= ex_day[1]:  # month
        if ac_day[0] <= ex_day[0]:  # day
            fine = 0
        else:
            if ac_day[1] < ex_day[1]:
                fine = 0
            else:
                fine = 15 * (int(ac_day[0]) - int(ex_day[0]))
    else:
        if ac_day[2] < ex_day[2]:
            fine = 0
        else:
            fine = 500 * (int(ac_day[1]) - int(ex_day[1]))
else:
    fine = 10000

print(fine)
