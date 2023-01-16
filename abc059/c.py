n = int(input())
a = list(map(int, input().split()))

total_cnt = 0
prev = a.pop(0)
for ai in a:
    # print(f"prev={prev}, ai={ai}, prev+ai={prev + ai}, total_cnt={total_cnt}")
    if prev > 0 and prev + ai >= 0:
        cnt = prev + ai + 1
        prev = prev + ai - cnt
        total_cnt += abs(cnt)
        continue
    elif prev < 0 and prev + ai <= 0:
        cnt = abs(prev + ai) + 1
        prev = prev + ai + cnt
        total_cnt += abs(cnt)
        continue
    prev += ai

print(total_cnt)
