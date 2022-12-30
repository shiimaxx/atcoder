N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

sum = 0
for i, ai in enumerate(a[:int(len(a) * 2 / 3)]):
    if i % 2 != 0:
        sum += ai

print(sum)
