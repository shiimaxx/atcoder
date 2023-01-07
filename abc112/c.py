N = int(input())
coordinates = []

for _ in range(N):
    x, y, h = map(int, input().split())
    coordinates.append([x, y, h])

sample = coordinates[0]

bucket = {}
for X in range(101):
    for Y in range(101):
        sample_x, sample_y, sample_h = coordinates[0][0], coordinates[0][1], coordinates[0][2]
        H = sample_h + abs(X - sample_x) + abs(Y - sample_y)
        for c in coordinates:
            x, y, h = c[0], c[1], c[2]
            if h == max([H - abs(X - x) - abs(Y - y), 0]):
                key = f"{X}_{Y}_{H}"
                if key not in bucket:
                    bucket[key] = 1
                else:
                    bucket[key] += 1

sorted_bucket = sorted(bucket.items(), key=lambda x: x[1], reverse=True)
print(' '.join(sorted_bucket[0][0].split('_')))
