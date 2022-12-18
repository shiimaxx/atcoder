N = int(input())
A = list(map(int, input().split()))

for i, a in enumerate(A[:]):
    for j in range(i):
        if a < A[j]:
            A[i] = A[j]
            A[j] = a

print(A[-1] - A[0])
