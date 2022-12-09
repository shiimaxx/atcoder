import math

N, A, B = map(int, input().split())

res = 0
for n in range(1, N+1):
    nn = n
    sum = 0
    while nn > 0:
        sum += nn % 10
        nn = math.floor(nn / 10)
    if A <= sum <= B:
        res += n

print(res)
