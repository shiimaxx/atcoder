n = int(input())
k = int(input())
c = [input() for _ in range(n)]
b = {}


def f(i, ci, num_cards):
    if num_cards >= k:
        if ci not in b:
            b[ci] = 0
        return
    for j in range(n):
        if i == j:
            continue
        f(i, ci + c[j], num_cards+1)


for i in range(n):
    f(i, c[i], 1)

print(b)
print(len(b.keys()))
