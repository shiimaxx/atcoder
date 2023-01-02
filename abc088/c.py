c = [[], [], []]
for i in range(3):
    ci = list(map(int, input().split()))
    c[i] = [ci[0] - ci[1], ci[1] - ci[2], ci[2] - ci[0]]

if c[0] == c[1] and c[1] == c[2] and c[2] == c[0]:
    print("Yes")
else:
    print("No")
