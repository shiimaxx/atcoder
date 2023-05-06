X, Y = map(int, input().split())
x = X
cnt = 0
while x <= Y:
    cnt += 1
    x *= 2

print(cnt)
