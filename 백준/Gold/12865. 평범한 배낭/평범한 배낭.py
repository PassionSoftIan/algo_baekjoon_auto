N, K = map(int, input().split())

DP_lst = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    weight, value = map(int, input().split())
    for j in range(1, K+1):
        if weight > j:
            DP_lst[i][j] = DP_lst[i-1][j]
        else:
            DP_lst[i][j] = max(value + DP_lst[i-1][j-weight], DP_lst[i-1][j])

print(DP_lst[N][K])