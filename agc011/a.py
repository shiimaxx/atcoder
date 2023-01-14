N, C, K = map(int, input().split())
T = []
for _ in range(N):
    T.append(int(input()))

bus_list = []
bus = []
for t in sorted(T):
    if len(bus) >= C or (len(bus) != 0 and bus[0] + K < t):
        bus_list.append(bus[:])
        bus = []
    bus.append(t)

if len(bus) > 0:
    bus_list.append(bus[:])

print(len(bus_list))
