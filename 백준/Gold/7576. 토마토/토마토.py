import sys
from collections import deque
input = sys.stdin.readline

def tomato(q):
    global c
    queue = deque(q)
    while queue:
        m, n, c = queue.popleft()
        for k in range(4):
            nx, ny = n + dx[k], m + dy[k]
            if 0 <= nx < M and 0 <= ny < N:
                if arr[ny][nx] == 0:
                    arr[ny][nx] = 1
                    queue.append([ny, nx, c + 1])


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = []
c = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append([i, j, c])
tomato(q)
for i in range(len(arr)):
    if 0 in arr[i]:
        print(-1)
        exit()
print(c)