N = int(input())
arr = list(map(int, input().split()))

count = 0
for i in range(N):
    if arr[i] != 1:
        bit = 0
        for j in range(2, arr[i]):
            if arr[i] % j == 0:
                bit = 1
                break
        if bit == 0:
            count += 1

print(count)