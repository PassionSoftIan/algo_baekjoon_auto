import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

want = [0]
for dck in range(Q):
    want.append(int(input()))

real_estate = [[] for _ in range(N+1)]

land = 0

for duck in range(1, len(want)):
    count = 0
    land = want[duck]
    while land != 1:
        if real_estate[land]:
            count = land
        land = land // 2
    if count == 0:
        real_estate[want[duck]].append(duck)
        print(0)
    else:
        print(count)