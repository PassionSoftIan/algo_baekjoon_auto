def solution(n, info):
    answer = []
    result = [0] * 11
    score = 0
    
    def backtracking(depth, target):
        nonlocal answer, score, result

        if depth == n:
            ryan = 0
            peach = 0

            for j in range(11):
                if result[j] > info[j]:
                    ryan += 10 - j
                if info[j] != 0 and result[j] <= info[j]:
                    peach += 10 - j

            if ryan > peach:
                if score < ryan-peach:
                    score = ryan-peach
                    answer = result[:]
                if score == ryan-peach:
                    for check in range(10, -1, -1):
                        if result[check] < answer[check]:
                            break
                        if result[check] > answer[check]:
                            answer = result[:]
                            break
            return

        for i in range(target, 11):
            result[i] += 1
            backtracking(depth+1, i)
            result[i] -= 1    

        
    backtracking(0, 0)
    if not answer:
        answer.append(-1)
    return answer