A, B = map(int, input().split())
print("Possible") if 0 in [A % 3, B % 3, (A + B) % 3] else print("Impossible")
