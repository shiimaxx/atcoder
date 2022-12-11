N, Y = map(int, input().split())

x, y, z = 0, 0, 0

for xx in range(0, N + 1):
    x = 10000 * xx
    for yy in range(0, (N + 1) - xx):
        y = 5000 * yy
        zz = (N - xx - yy)
        z = 1000 * zz
        if x + y + z == Y:
            print(f"{xx} {yy} {zz}")
            exit(0)

print("-1 -1 -1")
