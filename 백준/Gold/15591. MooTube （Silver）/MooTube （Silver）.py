import sys
from collections import deque
input = sys.stdin.readline
N, Q = map(int, input().split())

edge = [[] for _ in range(N+1)]

for nc in range(N-1):
    start, end, usado = map(int, input().split())
    edge[start].append([end, usado])
    edge[end].append([start, usado])

for qc in range(Q):
    K, num = map(int, input().split())
    keep = [0] * (N + 1)
    que = deque([[num, int(1e9)]])
    count = 0
    while que:
        node, node_ussado = que.popleft()
        keep[node] = 1
        for check in edge[node]:
            now = check[0]
            if keep[now] != 0:
                continue
            ussado = check[1]
            result = min(node_ussado, ussado)
            if K <= result:
                count += 1
                que.append([now, ussado])
                keep[now] = 1
    print(count)