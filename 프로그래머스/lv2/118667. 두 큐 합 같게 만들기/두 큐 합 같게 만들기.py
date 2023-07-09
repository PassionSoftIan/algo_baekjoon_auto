import copy
from collections import deque

def solution(queue1, queue2):
    que1 = deque(queue1)
    que2 = deque(queue2)
    
    q1 = copy.deepcopy(que1)
    q2 = copy.deepcopy(que2)
    
    sum1 = sum(que1)
    sum2 = sum(que2)
    
    length = len(queue1) * 3
    
    total = sum1 + sum2
    
    if total % 2 != 0:
        return -1
    
    count = 0
    while sum1 != sum2:
        if not que1 or not que2 or count == length:
            return -1
        if sum1 < sum2:
            go = que2.popleft()
            que1.append(go)
            sum1 += go
            sum2 -= go
            count += 1
            continue
        if sum1 > sum2:
            go = que1.popleft()
            que2.append(go)
            sum1 -= go
            sum2 += go
            count += 1
            continue
    return count