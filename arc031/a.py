Name = input()
ans = 'YES'
for i in range(int(len(Name) / 2)):
    if Name[i] != Name[-(i+1)]:
        ans = 'NO'
        break

print(ans)
