N, X = map(int, input().split())
m = [int(input()) for _ in range(N)]

X -= sum(m)
cnt = len(m)
cnt += X // min(m)
print(cnt)
