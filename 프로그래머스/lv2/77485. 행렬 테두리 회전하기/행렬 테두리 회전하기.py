def solution(rows, columns, queries):
    def BFS(y1, x1, y2, x2, check):
        nonlocal arr
        # if check % 2 == 0:
        stack = [[y1, x1]]
        count = 0
        result = []
        while stack:
            n, m = stack.pop()
            result.append(arr[n][m])
            if n == y1 and m == x1:
                count += 1
            if count == 2:
                answer.append(min(result))
                for ii in range(rows):
                    for jj in range(columns):
                        arr[ii][jj] = arr_2[ii][jj]
                return
            if n == y1 and m != x2:
                arr_2[n][m+1] = arr[n][m]
                stack.append([n, m+1])
            elif n != y2 and m == x2:
                arr_2[n+1][m] = arr[n][m]
                stack.append([n+1, m])
            elif n == y2 and m != x1:
                arr_2[n][m-1] = arr[n][m]
                stack.append([n, m-1])
            elif n != y1 and m == x1:
                arr_2[n-1][m] = arr[n][m]
                stack.append([n-1, m])
        
    answer = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    arr = [[] for _ in range(rows)]
    arr_2 = [[] for _ in range(rows)]
    
    count = 0
    for i in range(rows):
        for j in range(columns):
            count += 1
            arr[i].append(count)
            arr_2[i].append(count)
    
    for p in range(len(queries)):
        y1 = queries[p][0] - 1
        x1 = queries[p][1] - 1
        y2 = queries[p][2] - 1
        x2 = queries[p][3] - 1
        BFS(y1, x1, y2, x2, p)
        # for bb in range(rows):
        #     print(arr[bb])
            
            
    
    # print(arr)
    return answer