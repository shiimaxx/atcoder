def f(a, b, n):
    if n == 0:
        return a
    return f(b, a+b, n-1)


print(f(2, 1, int(input())))
