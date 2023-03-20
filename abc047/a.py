abc = list(map(int, input().split()))
print('Yes') if max(abc) == sum(abc) - max(abc) else print('No')
