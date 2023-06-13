N, K = map(int, input().split())

nums = list(map(int, input().split()))

visited = [0] * (max(nums) + 1)

result = 0

start = 0
end = 0

while start < N:
    if visited[nums[start]] != K:
        visited[nums[start]] += 1
        start += 1
    else:
        visited[nums[end]] -= 1
        end += 1
    if result < start - end:
        result = start - end

print(result)