n = int(input())
res = 1000000000
for h in range(1, n + 1):
    for w in range(1, int(n / h + 1)):
        res = min([res, abs(h - w) + (n - h * w)])

print(res)
