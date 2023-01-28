from decimal import Decimal
a, b, x = map(Decimal, input().split())
cnt = int((b - a) / x)
cnt = cnt + 1 if a % x == 0 else cnt
print(cnt)
