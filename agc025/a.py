N = int(input())

min = -1
for A in range(1, N):
    B = N - A

    a = 0
    if A < 10:
        a = A
    else:
        aa = A
        while aa > 0:
            a += aa % 10
            aa = int(aa / 10)

    b = 0
    if B < 10:
        b = B
    else:
        bb = B
        while bb > 0:
            b += bb % 10
            bb = int(bb / 10)

    if min == -1 or min > a + b:
        min = a + b
    # print(f"A={A}, B={B}, a={a}, b={b}, min={min}")

print(min)
