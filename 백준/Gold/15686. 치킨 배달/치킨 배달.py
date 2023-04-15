def backtracking(depth, s):
    if depth == M:
        check(result)
        return

    for c in range(s, len(chicken)):
        if visited[c] == 0:
            result.append(chicken[c])
            visited[c] = 1
            backtracking(depth+1, c)
            visited[c] = 0
            result.pop()


def check(rlt):
    info = [[int(1e9)]*N for _ in range(N)]
    chk = rlt
    for dis in home:
        for cc in chk:
            y, x = dis[0], dis[1]
            ny, nx = cc[0], cc[1]
            distance = abs(y-ny) + abs(x-nx)
            if info[y][x] > distance:
                info[y][x] = distance
    calculate(info)


def calculate(information):
    global min_result
    count = 0
    cal = information
    for a in range(N):
        for z in range(N):
            if cal[a][z] < int(1e9):
                count += cal[a][z]
    if min_result > count:
        min_result = count


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

chicken = []
home = []

result = []

min_result = int(1e9)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append([i, j])
        if arr[i][j] == 1:
            home.append([i, j])

visited = [0]*len(chicken)
backtracking(0, 0)

print(min_result)