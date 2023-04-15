import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

room = []

for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            room.append(arr[i][j])

if len(room) == 0:
    print(0)
    exit()

start = 0
end = max(room)
half = sum(room)
if half % 2 == 1:
    half = (half//2) + 1
else:
    half = (half//2)

result = 0

while start < end:
    mid = (start + end) // 2
    count = 0
    for computer in room:
        if computer <= mid:
            count += computer
        else:
            count += mid
    if count == half:
        print(mid)
        exit()

    if count < half:
        start = mid + 1
    else:
        end = mid
    result = end

print(result)