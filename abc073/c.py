N = int(input())
b = {}
for _ in range(N):
    A = int(input())
    b[A] = 1 if A not in b or b[A] == 0 else 0

print(sum([v for k, v in b.items()]))
