N = int(input())
A = list(map(int, input().split()))

seq = []
seq_list = []
check = None
for i, a in enumerate(A):
    if len(seq) == 0:
        seq.append(a)
        continue

    if check is None:
        if a - seq[-1] > 0:
            check = (lambda a: a >= 0)
        elif a - seq[-1] < 0:
            check = (lambda a: a <= 0)

    if check is None or check(a - seq[-1]):
        seq.append(a)
        continue

    seq_list.append(seq[:])
    seq = [a]
    check = None

if len(seq) > 0:
    seq_list.append(seq[:])

print(len(seq_list))
