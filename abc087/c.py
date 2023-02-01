N = int(input())
A = []
A.append(list(map(int, input().split())))
A.append(list(map(int, input().split())))

Aij = [[], []]
for i in range(2):
    c = 0
    for j, candy in enumerate(reversed(A[i])):
        c += candy
        Aij[i].insert(0, c)

i, j = 0, 0
s = A[i][j]
while j < N:
    if j == N-1 or Aij[i][j+1] < Aij[i+1][j]:
        s += sum(A[i+1][j:])
        break
    s += A[i][j+1]
    j += 1

print(s)
