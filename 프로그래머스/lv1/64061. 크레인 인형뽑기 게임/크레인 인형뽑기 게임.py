def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if stack:
                    check = stack.pop()
                    if check == board[j][i-1]:
                        answer += 2
                        board[j][i-1] = 0
                        break
                    else:
                        stack.append(check)
                        stack.append(board[j][i-1])
                        board[j][i-1] = 0
                        break
                else:
                    stack.append(board[j][i-1])
                    board[j][i-1] = 0
                    break
    print(stack)
                    
    return answer