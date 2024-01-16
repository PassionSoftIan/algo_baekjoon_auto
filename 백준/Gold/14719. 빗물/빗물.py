H, W = map(int, input().split())

arr = list(map(int, input().split()))

if arr[0] == 0 and arr[-1] == 0:
    print(0)
    exit()

result = 0

for i in range(1, W-1):
    l = max(arr[:i])
    r = max(arr[i+1:])
    min_high = min(l, r)
    if arr[i] < min_high:
        result += min_high - arr[i]

print(result)