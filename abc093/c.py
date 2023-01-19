A, B, C = map(int, input().split())

abc = sorted([A, B, C], reverse=True)
diff = (abc[0] - abc[1]) + (abc[0] - abc[2])

print(int(diff / 2)) if diff % 2 == 0 else print(int(diff / 2 + 2))
