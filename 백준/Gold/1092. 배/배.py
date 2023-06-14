N = int(input())
limits = list(map(int, input().split()))

M = int(input())
boxes = list(map(int, input().split()))

limits.sort()
boxes.sort()

count = 0

if boxes[-1] > limits[-1]:
    print(-1)
    exit()

while boxes:
    for limit in limits:
        if not boxes:
            break
        if limits[-1] < boxes[-1]:
            break
        else:
            for box in range(1, len(boxes) + 1):
                if boxes[-box] <= limit:
                    boxes.pop(-box)
                    break
    count += 1


print(count)