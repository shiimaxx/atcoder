A, B, C, D = map(int, input().split())
start = A if A > C else C
end = B if B < D else D
print(end - start if end >= start else 0)
