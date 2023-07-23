def solution(progresses, speeds):
    answer = []
    
    check = 0
    result = 0
    count = 1
    for i in range(len(progresses)):
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            result += 1
        if i == 0:
            check = result
            result = 0
        elif 0 < i < len(progresses) - 1:
            if check < result:
                answer.append(count)
                count = 1
                check = result
                result = 0
            elif check == result:
                count += 1
                result = 0
            else:
                count += 1
                result = 0
        else:
            if check < result:
                answer.append(count)
                answer.append(1)
                return answer
            else:
                answer.append(count + 1)
                return answer
    
    return answer