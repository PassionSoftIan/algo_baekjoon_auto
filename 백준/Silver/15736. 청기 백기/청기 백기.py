N = int(input())

count = 1
check = 3
i = 1
while check + i <= N:
    count += 1
    i += check
    check += 2

print(count)