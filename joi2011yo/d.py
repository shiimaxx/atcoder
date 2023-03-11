import itertools

n = int(input())
k = int(input())
c = [input() for _ in range(n)]
b = {}


def f(draw):
    for p in itertools.permutations(draw):
        s = ''
        for pp in p:
            s += c[pp]
        if s not in b:
            b[s] = 0


for i in range(2 ** n):
    if bin(i).count("1") == k:
        draw = []
        for j in range(n):
            if ((i >> j) & 1):
                draw.append(j)
        f(draw)

print(len(b.keys()))
