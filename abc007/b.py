A = input()
ans = -1
if len(list(A)) > 1:
    ans = ''.join(list(A)[:-1])
elif A != 'a':
    ans = chr(ord(A) - 1)

print(ans)
