A, B = map(int, input().split())

cnt = 0
for i in range(A, B+1):
    if i % 10 == int(i / 10000) and int(i / 10) % 10 == int(i / 1000) % 10:
        cnt += 1

print(cnt)
