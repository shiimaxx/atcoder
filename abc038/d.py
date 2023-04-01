import bisect

N = int(input())
wh = [list(map(int, input().split())) for _ in range(N)]
wh.sort(key=lambda x: (x[0], -x[1]))
# print(f"wh={wh}")

INF = 10 ** 7
dp = [INF for i in range(N+1)]
for i in range(N):
    # print(f"i={i}, bisect.bisect_left(dp, wh[i][1])={bisect.bisect_left(dp, wh[i][1])}")
    dp[bisect.bisect_left(dp, wh[i][1])] = wh[i][1]
# print(f"dp={dp}")
print(bisect.bisect_left(dp, INF))
