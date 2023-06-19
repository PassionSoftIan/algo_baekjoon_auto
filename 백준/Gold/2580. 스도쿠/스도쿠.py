def is_valid(row, col, num):
    for i in range(9):
        if arr[row][i] == num:
            return False

    for i in range(9):
        if arr[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if arr[i][j] == num:
                return False

    return True


def backtracking():
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(row, col, num):
                        arr[row][col] = num
                        if backtracking():
                            return True
                        arr[row][col] = 0
                return False
    return True


arr = []
while True:
    try:
        arr.append(list(map(int, input().split())))
    except:
        break

if backtracking():
    for row in arr:
        print(*row)