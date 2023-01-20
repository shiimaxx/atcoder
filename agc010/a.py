N = int(input())
A = list(map(int, input().split()))

while len(A) > 1:
    ai = A.pop(0)
    aj = 0
    for i, a in enumerate(A):
        if ai % 2 == a % 2:
            aj = a
            A.pop(i)
            break
    A.append(ai + aj)
    if len(A) == 2 and A[0] % 2 != A[1] % 2:
        print("NO")
        exit(0)

print("YES")
