N = int(input())
S = input()
res = -1
for i in range(1, N):
    X, Y = S[:i], S[i:]
    cnt = 0
    for x in set(X):
        if x in Y:
            cnt += 1
    if res < cnt:
        res = cnt

print(res)
