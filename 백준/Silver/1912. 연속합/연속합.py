import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

prefix_sum = [0] * N

prefix_sum[0] = arr[0]

for s in range(1, N):
    prefix_sum[s] = max(arr[s], prefix_sum[s - 1] + arr[s])

print(max(prefix_sum))