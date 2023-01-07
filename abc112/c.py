N = int(input())
coordinates = []

for _ in range(N):
    x, y, h = map(int, input().split())
    coordinates.append([x, y, h])

xx, yy, hh = -1, -1, -1
for c in coordinates:
    if c[2] != 0:
        xx, yy, hh = c[0], c[1], c[2]
        break

for X in range(101):
    for Y in range(101):
        H = hh + abs(X - xx) + abs(Y - yy)
        ok = True
        for c in coordinates:
            x, y, h = c[0], c[1], c[2]
            if h != max([H - abs(x - X) - abs(y - Y), 0]):
                ok = False
        if ok:
            print(X, Y, H)
            exit(0)
