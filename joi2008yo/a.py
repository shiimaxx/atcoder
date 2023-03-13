n = 1000 - int(input())
cnt = 0

while n >= 500:
    n -= 500
    cnt += 1
while n >= 100:
    n -= 100
    cnt += 1
while n >= 50:
    n -= 50
    cnt += 1
while n >= 10:
    n -= 10
    cnt += 1
while n >= 5:
    n -= 5
    cnt += 1

print(cnt+n)
