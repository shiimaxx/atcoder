N = int(input())
S = list(input())

W = []
cnt_w = 0
for s in S:
    cnt_w = cnt_w + 1 if s == 'W' else cnt_w
    W.append(cnt_w)

E = []
cnt_e = 0
for s in reversed(S):
    cnt_e = cnt_e + 1 if s == 'E' else cnt_e
    E.append(cnt_e)
E.reverse()

cnt_min = 3 * 10**5
for i in range(N):
    cnt = W[i] + E[i] - 1
    if cnt < cnt_min:
        cnt_min = cnt

print(cnt_min)
