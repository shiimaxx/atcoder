N = int(input())
t = [int(input()) for _ in range(N)]

min_times = 50 * 4
for i in range(2 ** N):
    times_a = 0
    times_b = 0
    for j in range(N):
        if ((i >> j) & 1):
            times_a += t[j]
        else:
            times_b += t[j]
    min_times = min(max(times_a, times_b), min_times)

print(min_times)
