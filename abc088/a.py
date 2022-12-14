N = int(input())
A = int(input())

n = N % 500
if n <= A:
    print('Yes')
    exit(0)

print('No')
