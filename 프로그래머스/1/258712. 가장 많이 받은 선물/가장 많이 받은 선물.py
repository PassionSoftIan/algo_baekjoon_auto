'''
1. 이번 달 까지 선물을 주고받은 기록이 있음.
2. 다음 달에 누가 선물을 많이 받을지 예측.
3. 두 사람 사이 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받음.
4. 주고 받지 않았거나 같은 개수를 주고 받았다면 선물 지수가 더 큰 사람이 선물을 하나 받음.
5. 선물지수 = (준 선물 총 수 - 받은 선물의 총 수)
6. 선물 지수까지 같으면 선물을 주고받지 않음.
'''

def solution(friends, gifts):
    answer = 0
    
    N = len(friends)
    M = len(gifts)
    
    gift_records = [[0] * N for _ in range(N)]
    gift_score = [0] * N
    
    for gift in gifts:
        send, receive = map(str, gift.split())
        
        send_friend_idx = 0
        receive_friend_idx = 0
        for i in range(N):
            if send == friends[i]:
                send_friend_idx = i
            
            if receive == friends[i]:
                receive_friend_idx = i
        
        gift_records[send_friend_idx][receive_friend_idx] += 1
        gift_score[send_friend_idx] += 1
        gift_score[receive_friend_idx] -= 1
    
    for i in range(N):
        next_month_receive_gfit_count = 0
        
        this_month_receive_gfit_count = 0
        this_month_send_gfit_count = 0
        for j in range(N):
            if i == j:
                continue
            if gift_records[i][j] > gift_records[j][i]:
                next_month_receive_gfit_count += 1
            
            elif gift_records[i][j] == gift_records[j][i]:
                if gift_score[i] > gift_score[j]:
                    next_month_receive_gfit_count += 1
                    
        answer = max(answer, next_month_receive_gfit_count)
    return answer