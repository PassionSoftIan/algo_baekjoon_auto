from collections import deque

S = int(input())

screen = 1
board = 0

que = deque([[1, 0, 0]])

visited = [[0]*(S+1) for _ in range(S+1)]

while que:
    n, m, c = que.popleft()
    if n + m == S or n - 1 == S:
        print(c+1)
        break
    if visited[n][n] == 0:
        que.append([n, n, c+1])
        visited[n][n] = 1
    if 0 <= n+m < S and visited[n+m][m] == 0:
        que.append([n+m, m, c+1])
        visited[n+m][m] = 1
    if 0 <= n-1 < S and visited[n-1][m] == 0:
        que.append([n-1, m, c+1])
        visited[n-1][m] = 1