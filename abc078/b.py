import math

X, Y, Z = map(int, input().split())
res = math.floor(X / (Y + Z))
print(res) if X % (Y + Z) >= Z else print(res - 1)
