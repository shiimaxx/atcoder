S = input()

while S != '':
    if S.endswith('dream'):
        S = S[:-5]
    elif S.endswith('dreamer'):
        S = S[:-7]
    elif S.endswith('erase'):
        S = S[:-5]
    elif S.endswith('eraser'):
        S = S[:-6]
    else:
        print('NO')
        exit(0)

print('YES')
