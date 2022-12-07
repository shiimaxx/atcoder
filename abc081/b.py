n = input()
a = list(map(int, input().split()))

cnt = 0


def extract_even(a):
    global cnt
    evens = []

    if len(a) < 1:
        return

    for aa in a:
        if aa % 2 != 0:
            return
        evens.append(aa / 2)
    cnt += 1
    extract_even(evens)


extract_even(a)

print(cnt)
