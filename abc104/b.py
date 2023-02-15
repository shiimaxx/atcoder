S = list(input())

check_A = False
check_C = False
check_other = True
for i, s in enumerate(S):
    if i == 0 and s == 'A':
        check_A = True
        continue

    if (i >= 2 and i <= len(S) - 2) and s == 'C' and not check_C:
        check_C = True
        continue

    if s.isupper():
        check_other = False
        break

print('AC') if check_A and check_C and check_other else print('WA')
