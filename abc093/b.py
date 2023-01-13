A, B, K = map(int, input().split())
for i in sorted(set([a for a in range(A, A+K) if a <= B] + [b for b in range(B, B-K, -1) if b >= A])):
    print(i)
