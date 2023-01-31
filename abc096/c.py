H, W = map(int, input().split())
s = []
for h in range(H):
    s.append(list(input()))

for i in range(H):
    for j in range(W):
        if s[i][j] == '.':
            continue

        top = s[i+1][j] if i < H-1 else '.'
        left = s[i][j-1] if j > 0 else '.'
        right = s[i][j+1] if j < W-1 else '.'
        bottom = s[i-1][j] if i > 0 else ','

        if top == '.' and left == '.' and right == '.' and bottom == '.':
            print('No')
            exit(0)

print('Yes')
