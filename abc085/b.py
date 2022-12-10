N = int(input())
dd = []
for n in range(N):
    d = int(input())
    if d not in dd:
        dd.append(d)

print(len(dd))
