s = input()

res = ''
for i, ss in enumerate(s):
    if (i+1) % 2 != 0:
        res += ss

print(res)
