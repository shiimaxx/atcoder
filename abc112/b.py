N, T = map(int, input().split())
min = 1001
for _ in range(N):
    c, t = map(int, input().split())
    if t <= T and c < min:
        min = c

print(min) if min < 1001 else print("TLE")
