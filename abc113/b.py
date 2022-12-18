N = int(input())
T, A = list(map(int, input().split()))
H = list(map(int, input().split()))

min_diff = -1
candidate = -1

for i, h in enumerate(H):
    a = T - h * 0.006
    diff = abs(A - a)
    if min_diff == -1 or min_diff > diff:
        min_diff = diff
        candidate = i+1

print(candidate)
