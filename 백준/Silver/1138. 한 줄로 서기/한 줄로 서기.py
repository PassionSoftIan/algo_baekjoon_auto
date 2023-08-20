N = int(input())
arr = list(map(int, input().split()))

check = [N] * N

for i in range(N):
    count = 0
    for j in range(N):
        if count == arr[i] and check[j] == N:
            check[j] = i + 1
            break
        if i + 1 < check[j]:
            count += 1
print(*check)