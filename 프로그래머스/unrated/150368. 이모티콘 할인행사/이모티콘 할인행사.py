def backtracking(depth, emoticons, sales, check, users, max_results):
    if depth == len(emoticons):            
        results = [0, 0]
        for user in users:
            cost = 0
            for cc in range(len(check)):
                if user[0] <= check[cc]:
                    cost += int(emoticons[cc] - emoticons[cc]*((check[cc])/100))
            if user[1] <= cost:
                results[0] += 1
            else:
                results[1] += cost

        if max_results[0] < results[0]:
            max_results[0] = results[0]
            max_results[1] = results[1]
        elif max_results[0] == results[0]:
            if max_results[1] < results[1]:
                max_results[1] = results[1]
        return
    for i in range(4):
        check[depth] = sales[i]
        backtracking(depth+1, emoticons, sales, check, users, max_results)

def solution(users, emoticons):
    answer = []
    sales = [10, 20, 30, 40]
    max_results = [0, 0]

    check = [0] * len(emoticons)
    
    backtracking(0, emoticons, sales, check, users, max_results)
        
    
    return max_results