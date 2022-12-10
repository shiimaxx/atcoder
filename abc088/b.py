N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

Alice, Bob = 0, 0

for i in range(0, N, 2):
    Alice += a[i]
    if i < N-1:
        Bob += a[i+1]

print(Alice - Bob)
