A, B, C = map(int, input().split())
a = 0
mod_list = []
while True:
    a += A
    mod = a % B
    if mod == C:
        print('YES')
        exit(0)
    elif mod in mod_list:
        print('NO')
        exit(0)
    mod_list.append(mod)
