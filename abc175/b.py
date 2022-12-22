N = int(input())
L = list(map(int, input().split()))

cnt = 0
for i, li in enumerate(L):
    LJ = L[i+1:]
    for j, lj in enumerate(LJ):
        LK = LJ[j+1:]
        for k, lk in enumerate(LK):
            if li == lj or li == lk or lj == lk:
                continue
            s = sorted([li, lj, lk])
            # 他の2本の棒の長さ > 最も長い棒の長さ
            if s[0] + s[1] > s[2]:
                cnt += 1

print(cnt)
