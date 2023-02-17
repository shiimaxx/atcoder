N = int(input())
n = N
while True:
    if n % 2 == 0 and n % N == 0:
        print(n)
        exit(0)
    n += N
