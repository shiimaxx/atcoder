A, B = map(int, input().split())
S = input()

a, h, b = S[:A], S[A:A+1], S[A+1:]
if a.isdigit() and h == '-' and b.isdigit():
    print('Yes')
else:
    print('No')
