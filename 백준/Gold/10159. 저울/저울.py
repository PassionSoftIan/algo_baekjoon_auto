import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

edge = [[] for _ in range(N+1)]

for mc in range(M):
    start, end = map(int, input().split())
    edge[start].append(end)

visited = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    stack = [i]
    count = 0
    while stack:
        n = stack.pop()
        if visited[i][n] == 0:
            if edge[n]:
                for j in range(len(edge[n])):
                    stack.append(edge[n][j])
            visited[i][n] = 1
            visited[n][i] = 1

for i in range(1, N+1):
    count = 0
    for j in range(1, N+1):
        if visited[i][j] == 0:
            count += 1
    print(count)