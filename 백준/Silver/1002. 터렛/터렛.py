import math

Test_Case = int(input())

for tc in range(Test_Case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif r1 + r2 == dist or abs(r1 - r2) == dist:
        print(1)
    elif abs(r1-r2) < dist < (r1+r2):
        print(2)
    else:
        print(0)