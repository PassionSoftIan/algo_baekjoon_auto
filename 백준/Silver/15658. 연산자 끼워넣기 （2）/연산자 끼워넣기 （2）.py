N = int(input())

num = list(map(int, input().split()))
operation = list(map(int, input().split()))
count = 0
max_result = 0
min_result = 0

def operate(depth, total, plus, minus, multiple, divide):
    global count, max_result, min_result
    if depth == N:
        if count == 0:
            max_result = total
            min_result = total
        else:
            if max_result < total:
                max_result = total

            if min_result > total:
                min_result = total
        count += 1
        return

    if plus > 0:
        operate(depth+1, total+num[depth], plus-1, minus, multiple, divide)

    if minus > 0:
        operate(depth+1, total-num[depth], plus, minus-1, multiple, divide)

    if multiple > 0:
        operate(depth+1, total*num[depth], plus, minus, multiple-1, divide)

    if divide > 0:
        operate(depth+1, int(total/num[depth]), plus, minus, multiple, divide-1)

operate(1, num[0], operation[0], operation[1], operation[2], operation[3])

print(max_result)
print(min_result)