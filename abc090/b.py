A, B = map(int, input().split())

cnt = 0
for i in range(A, B+1):
    istr = str(i)
    if istr[0] == istr[4] and istr[1] == istr[3]:
        cnt += 1
print(cnt)
