import re

S, T = input(), input()
result = 'UNRESTORABLE'
for i in range(0, len(S) - len(T) + 1):
    S_ = S[:]
    pt = S_[i:i+len(T)].replace('?', '.')
    if re.match(pt, T):
        S_ = list(S_)
        S_[i:i+len(T)] = T
        S_ = "".join(S_)
        S_ = S_.replace('?', 'a')
        if result == 'UNRESTORABLE' or S_ < result:
            result = S_

print(result)
