from collections import deque

dy = [0, 1, 1]
dx = [1, 1, 0]

def solution(m, n, board):
    answer = 0
    N = m
    M = n
    arr = []
    
    for block in board:
        go = []
        for bc in range(len(block)):
            go.append(block[bc])
        arr.append(go)
    # for i in arr:
    #     print('first', i)
    
    while True :
        destroy = []
        for i in range(N):
            for j in range(M):
                count = 0
                temp = []
                temp.append([i, j])
                for k in range(3):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0 <= ny < N and 0 <= nx < M:
                        if arr[i][j] != 0 and arr[i][j] == arr[ny][nx]:
                            temp.append([ny, nx])
                            count += 1
                if count == 3:
                    while temp:
                        destroy.append(temp.pop())

        if not destroy:
            break
                        
        while destroy:
            fy, fx = destroy.pop()
            if arr[fy][fx] != 0:
                arr[fy][fx] = 0
                answer += 1

        for p in range(M):
            change = deque([])
            for z in range(N-1, -1, -1):
                if arr[z][p] == 0:
                    change.append([z, p])
                else:
                    if change:
                        cn, cm = change.popleft()
                        arr[cn][cm] = arr[z][p]
                        arr[z][p] = 0
                        change.append([z, p])
    
    # for i in range(N):
    #     for j in range(M):
    #         if arr[i][j] == 0:
    #             answer += 1
    
    # for i in destroy:
    #     print(i)
    # for i in arr:
    #     print('after', i)
    
    return answer