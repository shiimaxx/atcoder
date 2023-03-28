import math

ab = int(''.join(input().split()))
print('Yes') if math.sqrt(ab) % 1 == 0.0 else print('No')
