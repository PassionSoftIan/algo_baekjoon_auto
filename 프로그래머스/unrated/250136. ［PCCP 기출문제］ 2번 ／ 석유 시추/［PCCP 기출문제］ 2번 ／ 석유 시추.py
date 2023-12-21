from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def solution(land):
    N = len(land)
    M = len(land[0])
    
    visited = [[0] * M for _ in range(N)]
    check = [0] * M
    
    def bfs(que):    
        q = deque([que])
        count = 1
        result = []
        while q:
            n, m = q.popleft()
            if m not in result:
                result.append(m)
            for k in range(4):
                ny = n + dy[k]
                nx = m + dx[k]
                if 0 <= ny < N and 0 <= nx < M:
                    if land[ny][nx] == 1 and visited[ny][nx] == 0:
                        q.append([ny, nx])
                        visited[ny][nx] = 1
                        count += 1
        while result:
            line = result.pop()
            check[line] += count

    for i in range(N):
        for j in range(M):
            if land[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                bfs([i, j])

    return max(check)