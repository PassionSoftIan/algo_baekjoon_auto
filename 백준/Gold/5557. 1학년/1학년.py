N = int(input())

numbers = list(map(int, input().split()))

DP = [[0] * 21 for _ in range(N-1)]

DP[0][numbers[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        if DP[i-1][j]:
            if 0 <= j + numbers[i] <= 20:
                DP[i][j + numbers[i]] += DP[i-1][j]
            if 0 <= j - numbers[i] <= 20:
                DP[i][j - numbers[i]] += DP[i-1][j]

print(DP[N-2][numbers[N-1]])