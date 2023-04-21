A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if b == A[i][j]:
                A[i][j] = -1

result = 'No'
for i in range(3):
    if sum(A[i]) == -3:
        result = 'Yes'
        break
    if sum([A[0][i], A[1][i], A[2][i]]) == -3:
        result = 'Yes'
        break

if sum([A[0][0], A[1][1], A[2][2]]) == -3:
    result = 'Yes'

if sum([A[0][2], A[1][1], A[2][0]]) == -3:
    result = 'Yes'

print(result)
