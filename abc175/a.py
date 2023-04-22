S = input()
r, res = 0, 0
for s in S:
    r = r + 1 if s == 'R' else 0
    res = r if res < r else res
print(res)
