import math

N, D = map(int, input().split())
X = []

for _ in range(N):
    x = list(map(int, input().split()))
    X.append(x)

res = 0
for i, x in enumerate(X):
    for xx in X[i+1:]:
        sum = 0
        for d in range(D):
            sum += (x[d] - xx[d]) ** 2
        sqrt_sum = math.sqrt(sum)
        if sqrt_sum.is_integer():
            res += 1

print(res)
