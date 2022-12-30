N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

sum = 0
while len(a) > 0:
    a.pop(0)
    sum += a.pop(0)
    a.pop()

print(sum)
