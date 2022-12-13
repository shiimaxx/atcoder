N = int(input())
curr_t, curr_x, curr_y = 0, 0, 0

t = []
x = []
y = []

for i in range(N):
    txy = list(map(int, input().split()))
    t.append(txy[0])
    x.append(txy[1])
    y.append(txy[2])

for i in range(N):
    tt, xx, yy = t[i], x[i], y[i]
    distance = abs((xx + yy) - (curr_x + curr_y))
    remain_t = tt - curr_t

    if distance > remain_t or (remain_t - distance) % 2 != 0:
        print('No')
        exit(0)
    curr_t, curr_x, curr_y = tt, xx, yy

print('Yes')
