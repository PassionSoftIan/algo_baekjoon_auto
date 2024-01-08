N = int(input())

result = []
for tc in range(N):
    arr = sorted(list(map(int, input().split())))
    M = len(arr)
    max_result = 0
    for i in range(M - 1):
        for j in range(i + 1, M):
            a = arr[j]
            b = arr[i]
            while b != 0:
                temp_a = a
                a = b
                b = temp_a % b
            if max_result < a:
                max_result = a
    result.append(max_result)

for check in result:
    print(check)