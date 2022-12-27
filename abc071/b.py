import string

S = input()
found = {}
for s in S:
    found[s] = None

for s in string.ascii_lowercase:
    if s not in found:
        print(s)
        exit(0)

print("None")
