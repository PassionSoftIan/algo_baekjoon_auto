def dfs(stack, arr, visited):
    count = 0
    stk = [stack]
    while stk:
        n = stk.pop()
        for i in range(len(arr[n])):
            if visited[n][i] == 0 and arr[n][i] == 1:
                stk.append(i)
                visited[n][i] = 1
                visited[i][n] = 1

    count += 1
    return count
                

def solution(N, arr):
    answer = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        visited[i][i] = 1

    for i in range(N):
        check = 0
        for j in range(N):
            if visited[i][j] == 0 and arr[i][j] == 1:
                visited[i][j] = 1
                visited[j][i] = 1
                answer += dfs(j, arr, visited)
            if arr[i][j] == 0:
                check += 1
        if check == N-1:
            answer += 1
    return answer