import math

N = int(input())

min = -1
for A in range(1, int(math.sqrt(N)+1)):
    if N % A != 0:
        continue
    B = int(N / A)
    digit = len(str(A)) if len(str(A)) > len(str(B)) else len(str(B))
    if min == -1 or digit < min:
        min = digit

print(min)
