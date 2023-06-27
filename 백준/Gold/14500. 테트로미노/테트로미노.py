dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

check = {0: 1, 1: 0, 2: 3, 3: 2}
check_2 = {0: 1, 1: 2, 2: 3, 3: 0}


def first(stack):
    global result_max
    stk = [stack]
    while stk:
        n, m = stk.pop()
        for k in range(4):
            count = 0
            for l in range(4):
                ny, nx = n + l*dy[k], m + l*dx[k]
                if 0 <= ny < N and 0 <= nx < M:
                    count += arr[ny][nx]
            if result_max < count:
                result_max = count


def second(depth, stack):
    global result_max
    if depth == 3:
        if result_max < stack[2]:
            result_max = stack[2]
        return

    stk = [stack]
    n, m, c = stk.pop()
    ny, nx = n + dy[depth], m + dx[depth]
    if 0 <= ny < N and 0 <= nx < M:
        c += arr[ny][nx]
    second(depth+1, [ny, nx, c])


def third(depth, stack):
    global result_max
    n = stack[0]
    m = stack[1]
    count = 0

    if depth == 8:
        return
    if depth == 0 or depth == 6:
        if 0 <= n - 1 < N:
            count = arr[n-1][m]
    if depth == 1 or depth == 7:
        if 0 <= m - 1 < M:
            count = arr[n][m-1]
    if depth == 2 or depth == 4:
        if 0 <= n + 1 < N:
            count = arr[n+1][m]
    if depth == 3 or depth == 5:
        if 0 <= m + 1 < M:
            count = arr[n][m+1]
    for l in range(3):
        ny, nx = n + l*dy[depth % 4], m + l*dx[depth % 4]
        if 0 <= ny < N and 0 <= nx < M:
            count += arr[ny][nx]
    if result_max < count:
        result_max = count
    third(depth+1, stack)


def fourth(depth, stack):
    global result_max
    n = stack[0]
    m = stack[1]
    count = 0

    if depth == 4:
        return
    if depth == 0:
        if 0 <= n - 1 < N:
            count = arr[n-1][m]
    if depth == 1:
        if 0 <= m + 1 < M:
            count = arr[n][m+1]
    if depth == 2:
        if 0 <= n + 1 < N:
            count = arr[n+1][m]
    if depth == 3:
        if 0 <= m - 1 < M:
            count = arr[n][m-1]
    for l in range(2):
        ny, nx = n + l*dy[depth % 2], m + l*dx[depth % 2]
        if 0 <= ny < N and 0 <= nx < M:
            count += arr[ny][nx]
        if l == 1:
            if 0 <= ny+dy[check_2[depth]] < N and 0 <= nx+dx[check_2[depth]] < M:
                count += arr[ny+dy[check_2[depth]]][nx+dx[check_2[depth]]]
    if result_max < count:
        result_max = count
    fourth(depth+1, stack)


def fifth(depth, stack):
    global result_max
    n = stack[0]
    m = stack[1]
    count = 0

    if depth == 4:
        return
    for l in range(3):
        ny, nx = n + l*dy[depth % 2], m + l*dx[depth % 2]
        if 0 <= ny < N and 0 <= nx < M:
            count += arr[ny][nx]
        if l == 1:
            if 0 <= ny+dy[check[depth]] < N and 0 <= nx+dx[check[depth]] < M:
                count += arr[ny+dy[check[depth]]][nx+dx[check[depth]]]
    if result_max < count:
        result_max = count
    fifth(depth+1, stack)


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

result_max = 0


for i in range(N):
    for j in range(M):
        first([i, j])
        second(0, [i, j, arr[i][j]])
        third(0, [i, j])
        fourth(0, [i, j])
        fifth(0, [i, j])

print(result_max)