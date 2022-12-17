N = int(input())

for cake in range(int(N / 4) + 1):
    for donut in range(int(N / 7) + 1):
        if N == (cake * 4) + (donut * 7):
            print('Yes')
            exit(0)

print('No')
