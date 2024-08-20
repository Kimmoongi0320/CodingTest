def solution(matrix1, matrix2):
    arr = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                arr[i][j] += matrix1[i][k] * matrix2[k][j]

    # 바꿀 것만 바꾸기
    for i in range(2):
        for j in range(i, 3):
            num = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = num

    return arr


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
