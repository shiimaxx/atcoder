S = input()


def f(pre, s):
    total = 0
    for i in range(1, len(s)+1):
        first_half = int(s[:i]) if s[:i] != '' else 0
        second_half = s[i:]
        total += pre + first_half + int(second_half) if len(second_half) > 0 else 0
        total += f(pre + first_half, second_half)
    return total


print(f(0, S) + int(S))
