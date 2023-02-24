N = int(input())
total = 0
for m in map(int, input().split()):
    total += 80 - m if m < 80 else 0
print(total)
