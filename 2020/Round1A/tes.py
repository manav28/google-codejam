import os
"""from math import log10, floor
def get_answer(U):
    char_pred = {}
    for _ in range(10**4):
        m, r = input().split()
        m = int(m)
        num_digits_m = floor(log10(m)) + 1
        if len(r) == num_digits_m:
            msd = m // (10 ** (num_digits_m - 1))
            code = r[0]
            if code in char_pred:
                char_pred[code] = min(char_pred[code], msd)
            else:
                char_pred[code] = msd
    char_pred = {ch:i for ch, i in sorted(char_pred.items(), key=lambda x: x[1])}
    return "".join(list(char_pred.keys()))

tests = int(input())
for t in range(1, tests+1):
    U = int(input())
    ans = get_answer(U)
    print("Case #{}: {}".format(t, ans))"""
print(os.getcwd())
with open("Round1A/test.txt", 'r') as f:
    l = f.readlines()
d = {}
for line in l:
    ch = line.split()[1][0]
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] += 1
d = {k:v for k, v in sorted(d.items(), key=lambda x: -x[1])}
for line in l:
    flag = False
    code = line.split()[1]
    for ch in code:
        if ch not in d:
            zero = ch
            flag = True
            break
    if flag:
        break
print(zero + "".join(list(d.keys())))