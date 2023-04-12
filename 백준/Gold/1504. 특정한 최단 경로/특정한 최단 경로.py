import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def dijkstra(go):
    visited = [int(1e9)] * (N + 1)
    visited[go[1]] = 0
    heap = []
    heappush(heap, go)
    while heap:
        cost, now = heappop(heap)
        if visited[now] < cost:
            continue
        for check in edge[now]:
            total = cost + check[0]
            if total < visited[check[1]]:
                visited[check[1]] = total
                heappush(heap, [total, check[1]])
    return visited


N, E = map(int, input().split())

edge = [[] for _ in range(N+1)]

for node in range(E):
    start, end, distance = map(int, input().split())
    edge[start].append([distance, end])
    edge[end].append([distance, start])

exam_node1, exam_node2 = map(int, input().split())

a = dijkstra([0, 1])
b = dijkstra([0, exam_node1])
c = dijkstra([0, exam_node2])

result1 = a[exam_node1] + b[exam_node2] + c[N]
result2 = a[exam_node2] + c[exam_node1] + b[N]

if result1 >= int(1e9) and result2 >= int(1e9):
    print(-1)
else:
    print(min(result1, result2))