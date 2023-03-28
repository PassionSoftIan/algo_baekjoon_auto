import sys
input = sys.stdin.readline

def check(start):
    global count, now
    if now > score_lst[start][1]:
        count += 1
        now = score_lst[start][1]
        return

Test_case = int(input())

for tc in range(1, Test_case+1):
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(N)]
    score_lst = sorted(score)
    count = 1
    now = score_lst[0][1]
    for i in range(1, N):
        check(i)

    print(count)