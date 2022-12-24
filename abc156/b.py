N, K = map(int, input().split())

cnt = 1
while True:
    min, max = K ** (cnt - 1), (K ** (cnt)) - 1
    # print(cnt, min, max)
    if min <= N and N <= max:
        break
    cnt += 1

print(cnt)
