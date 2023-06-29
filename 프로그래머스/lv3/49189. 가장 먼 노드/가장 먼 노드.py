from collections import deque

def solution(n, vertex):
    answer = 0
    edge = [[] for _ in range(n + 1)]
    
    for i in vertex:
        edge[i[0]].append(i[1])
        edge[i[1]].append(i[0])
    
    visited = [0] * (n+1)
    visited[1] = 1
    
    que = deque([1])
    
    while que:
        node = que.popleft()
        
        for i in edge[node]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = visited[node] + 1
    
    for result in visited:
        if result == max(visited):
            answer += 1
    
    
    return answer