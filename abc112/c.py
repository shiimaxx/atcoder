N = int(input())
coordinates = [[0 for _ in range(10)] for _ in range(10)]

for _ in range(N):
    x, y, h = map(int, input().split())
    coordinates[x][y] = h

for c in coordinates:
    print(c)
