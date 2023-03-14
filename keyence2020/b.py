N = int(input())
XL = [list(map(int, input().split())) for _ in range(N)]
XL.sort(key=lambda x: x[0]+x[1])

cnt = 0
last = -1000000000
for x, l in XL:
    if last <= x-l:
        cnt += 1
        last = x+l

print(cnt)
