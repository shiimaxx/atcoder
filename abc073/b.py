cnt = 0
for _ in range(int(input())):
    l, r = map(int, input().split())
    cnt += r - l + 1

print(cnt)
