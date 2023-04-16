A = sorted(list(map(int, input().split())))
cost = 0
for i in range(1, 3):
    cost += abs(A[i] - A[i-1])
print(cost)
