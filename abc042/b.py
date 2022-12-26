N, L = map(int, input().split())
S = []

for _ in range(N):
    S.append(input())

S.sort()
print(''.join(S))
