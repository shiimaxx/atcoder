D, G = map(int, input().split())
p, c = [], []
for i in range(D):
    pi, ci = map(int, input().split())
    p.append(pi)
    c.append(ci)

min_answers = D ** 100
for i in range(2 ** D):
    score = 0
    answers = 0
    rest_max = -1
    for j in range(D):
        if ((i >> j) & 1):
            score += (p[j] * ((j + 1) * 100 )) + c[j]
            answers += p[j]
        else:
            rest_max = j

    if score < G:
        s1 = 100 * (rest_max + 1)
        need = int((G - score + s1 - 1) / s1)
        if need >= p[rest_max]:
            continue
        answers += need
    min_answers = min(min_answers, answers)

print(min_answers)
