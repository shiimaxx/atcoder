N = int(input())
s = sum([int(i) for i in list(str(N))])
print('Yes') if N % s == 0 else print('No')
