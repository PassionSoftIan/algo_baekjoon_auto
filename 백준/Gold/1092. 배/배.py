N = int(input())
limits = list(map(int, input().split()))

M = int(input())
boxes = list(map(int, input().split()))

limits.sort(key=lambda x: x, reverse=True)
boxes.sort(key=lambda x: x, reverse=True)

count = 0

if boxes[0] > limits[0]:
    print(-1)
    exit()

while boxes:
    for limit in limits:
        if not boxes:
            break
        if limits[0] < boxes[0]:
            break
        else:
            for box in range(len(boxes)):
                if boxes[box] <= limit:
                    boxes.pop(box)
                    break
    count += 1


print(count)