S, T = input(), input()
for i in range(len(S)):
    if ''.join(S[i:] + S[:i]) == T:
        print('Yes')
        exit(0)
print('No')
