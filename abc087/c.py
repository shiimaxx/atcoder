N = int(input())
A = []
A.append(list(map(int, input().split())))
A.append(list(map(int, input().split())))

max_cnt = 0
j = 0
while j < N:
    candies = []
    i = 0
    for n in range(N):
        if n == j:
            candies.append(A[i][n])
            i += 1
        candies.append(A[i][n])
    cnt = sum(candies)
    if cnt > max_cnt:
        max_cnt = cnt
    j += 1

print(max_cnt)
