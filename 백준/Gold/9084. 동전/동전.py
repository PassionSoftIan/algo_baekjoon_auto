Test_case = int(input())

for tc in range(1, Test_case+1):
    N = int(input())
    coin = list(map(int, input().split()))
    money = int(input())

    DP = [0] * (money + 1)
    DP[0] = 1

    for c in coin:
        for i in range(1, money + 1):
            if i >= c:
                DP[i] += DP[i-c]

    print(DP[money])