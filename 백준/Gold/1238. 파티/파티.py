import sys
input = sys.stdin.readline
from heapq import heappop, heappush


def dijkstra(first, check):
    q = []
    heappush(q, first)
    while q:
        dist, now = heappop(q)
        if visited[check][now] < dist:
            continue
        for i in edge[now]:
            total = dist + i[0]
            if total < visited[check][i[1]]:
                visited[check][i[1]] = total
                heappush(q, [total, i[1]])


N, M, X = map(int, input().split())

edge = [[] for _ in range(N+1)]

visited = [[int(1e9)]*(N+1) for _ in range(N+1)]

for mc in range(M):
    start, end, distance = map(int, input().split())
    edge[start].append([distance, end])

max_count = 0
for d in range(1, N+1):
    visited[d][d] = 0
    dijkstra([0, d], d)

for i in range(1, N+1):
    chk = visited[i][X] + visited[X][i]
    if max_count < chk:
        max_count = chk

print(max_count)
