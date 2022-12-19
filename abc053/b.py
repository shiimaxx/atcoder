s = input()

start, end = -1, -1

for i, ss in enumerate(s):
    if start == -1 and ss == 'A':
        start = i

    if start != -1 and ss == 'Z':
        end = i

print(end - start + 1)
