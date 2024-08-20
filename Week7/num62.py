def rotation(length, arr):
    new_board = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            new_board[j][length - i - 1] = arr[i][j]
    return new_board


def solution(arr, n):
    length = len(arr)
    for _ in range(n):
        arr = rotation(length, arr)
    return arr


print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 1))
