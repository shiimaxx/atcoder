A, B = map(int, input().split())
res = 0
for i in range(1, B):
    if A * i - (i - 1) >= B:
        res = i
        break
print(res)
