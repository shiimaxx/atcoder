N = int(input())
X = list(map(int, input().split()))

total = 100000000
for i in range(1, max(X)+1):
    tmp_total = 0
    for x in X:
        tmp_total += (x - i) ** 2
    if total > tmp_total:
        total = tmp_total

print(total)
