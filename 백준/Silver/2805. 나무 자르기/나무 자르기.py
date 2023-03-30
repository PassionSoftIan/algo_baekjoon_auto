import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

top = 1
low = max(arr)

while top <= low:
    mid = (top + low) // 2
    count = 0
    for i in arr:
        if i > mid:
            count += i - mid

    if count >= M:
        top = mid + 1

    else:
        low = mid - 1

print(low)