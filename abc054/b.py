N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(M)]


def match(a, b):
    for i in range(M):
        for j in range(M):
            if a[i][j] != b[i][j]:
                return False
    return True


result = False
for i in range(N-M+1):
    for j in range(N-M+1):
        print(i, j)
        aa = [a[j:j+M] for a in A[i:i+M]]
        if match(aa, B):
            result = True

print('Yes') if result else print('No')
