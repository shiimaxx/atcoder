import sys
sys.setrecursionlimit(1000000)

H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]
r = [[False for _ in range(W)] for _ in range(H)]
gi, gj = -1, -1
si, sj = -1, -1
for i, h in enumerate(c):
    for j, w in enumerate(h):
        if w == 'g':
            gi, gj = i, j
        elif w == 's':
            si, sj = i, j


def search(x, y):
    if x < 0 or H <= x or y < 0 or W <= y or c[x][y] == '#':
        return
    if r[x][y]:
        return

    r[x][y] = True

    search(x + 1, y)
    search(x - 1, y)
    search(x, y + 1)
    search(x, y - 1)


search(si, sj)
print('Yes') if r[gi][gj] else print('No')
