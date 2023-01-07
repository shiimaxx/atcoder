N = int(input())
coordinates = []

for _ in range(N):
    x, y, h = map(int, input().split())
    coordinates.append([x, y, h])

bucket = {}
for X in range(101):
    for Y in range(101):
        for H in range(200):
            for c in coordinates:
                x, y, h = c[0], c[1], c[2]
                if h == max([H - abs(X - x) - abs(Y - y), 0]):
                    key = f"{X}_{Y}_{H}"
                    if key not in bucket:
                        bucket[key] = 1
                    else:
                        bucket[key] += 1

max = 0
max_k = ''
for k, v in bucket.items():
    if max == 0 or max < v:
        max = v
        max_k = k

print(' '.join(max_k.split('_')))
