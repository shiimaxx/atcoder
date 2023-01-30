N = int(input())
a = [int(input()) for _ in range(N)]

cnt = 0
b = 1
hist = [b]
while b != 2:
    b = a[b-1]
    if b in hist:
        cnt = -1
        break
    cnt += 1
    hist.append(b)

print(cnt)
