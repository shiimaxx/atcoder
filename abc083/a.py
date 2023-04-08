A, B, C, D = map(int, input().split())
print('Left') if A + B > C + D else print('Right') if A + B < C + D else print('Balanced')
