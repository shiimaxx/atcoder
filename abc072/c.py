N = int(input())
a = list(map(int, input().split()))
b = {}
for ai in a:
    b[ai] = b[ai] + 1 if ai in b else 1
    b[ai+1] = b[ai+1] + 1 if ai+1 in b else 1
    b[ai-1] = b[ai-1] + 1 if ai-1 in b else 1

X = sorted(b.items(), key=lambda i: i[1], reverse=True)[0][0]

cnt = 0
for ai in a:
    if ai in [X, X+1, X-1]:
        cnt += 1

print(cnt)
