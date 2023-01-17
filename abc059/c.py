n = int(input())
a = list(map(int, input().split()))
first = a.pop(0)

cnt, total_cnt1 = 0, 0
if first > 0:
    prev = first
else:
    prev = 1
    total_cnt1 += abs(first) + 1

for ai in a:
    # print(f"prev={prev}, ai={ai}, prev+ai={prev + ai}, total_cnt={total_cnt}")
    if prev > 0 and prev + ai >= 0:
        cnt = prev + ai + 1
        prev = prev + ai - cnt
        total_cnt1 += abs(cnt)
    elif prev < 0 and prev + ai <= 0:
        cnt = abs(prev + ai) + 1
        prev = prev + ai + cnt
        total_cnt1 += abs(cnt)
    else:
        prev += ai

cnt, total_cnt2 = 0, 0
if first < 0:
    prev = first
else:
    prev = -1
    total_cnt2 += abs(first) + 1

for ai in a:
    # print(f"prev={prev}, ai={ai}, prev+ai={prev + ai}, total_cnt={total_cnt}")
    if prev > 0 and prev + ai >= 0:
        cnt = prev + ai + 1
        prev = prev + ai - cnt
        total_cnt2 += abs(cnt)
    elif prev < 0 and prev + ai <= 0:
        cnt = abs(prev + ai) + 1
        prev = prev + ai + cnt
        total_cnt2 += abs(cnt)
    else:
        prev += ai

print(total_cnt1) if total_cnt1 <= total_cnt2 else print(total_cnt2)
