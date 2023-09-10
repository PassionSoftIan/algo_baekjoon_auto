def solution(targets):
    answer = 1
    targets.sort(key = lambda x : x[1])
    
    fire = targets[0][1]
    for i in range(1, len(targets)):
        if fire <= targets[i][0]:
            fire = targets[i][1]
            answer += 1
    
    # print(targets)
    # print(answer)
    
    return answer