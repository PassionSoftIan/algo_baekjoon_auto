N, K = map(int, input().split())

item = [list(map(int, input().split())) for _ in range(N)]

DP_lst = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(N+1):
    for j in range(K+1):
        if i == 0 or j == 0:
            DP_lst[i][j] = 0

        elif item[i-1][0] <= j:
            DP_lst[i][j] = max(item[i-1][1] + DP_lst[i-1][j-item[i-1][0]],
                               DP_lst[i-1][j])
        else:
            DP_lst[i][j] = DP_lst[i-1][j]

print(DP_lst[N][K])