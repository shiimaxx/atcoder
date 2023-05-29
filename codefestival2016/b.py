N, A, B = map(int, input().split())
S = list(input())

qA, qB = [], []

for i in range(len(S)):
    if S[i] == 'a' and len(qA) + len(qB) < A + B:
        qA.append(i)
        print('Yes')
    elif S[i] == 'b' and len(qA) + len(qB) < A + B and len(qB) + 1 <= B:
        qB.append(i)
        print('Yes')
    else:
        print('No')
