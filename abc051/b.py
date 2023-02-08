K, S = map(int, input().split())
cnt = 0
for X in range(K+1):
    for Y in range(K+1):
        Z = S - (X + Y)
        if Z >= 0 and Z <= K:
            cnt += 1

print(cnt)
