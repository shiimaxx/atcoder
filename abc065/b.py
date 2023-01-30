N = int(input())
a = [int(input()) for _ in range(N)]
hist = [0 for _ in range(N)]

cnt = 0
b = 1
while b != 2:
    b = a[b-1]
    if hist[b-1] == 1:
        cnt = -1
        break
    cnt += 1
    hist[b-1] = 1

print(cnt)
