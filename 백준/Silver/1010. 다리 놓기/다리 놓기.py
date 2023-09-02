def count_bridges(N, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # 초기값 설정
    for i in range(M + 1):
        dp[1][i] = i

    for i in range(2, N + 1):
        for j in range(i, M + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

    return dp[N][M]

Test_case = int(input())

for tc in range(Test_case):
    N, M = map(int, input().split())
    result = count_bridges(N, M)
    print(result)