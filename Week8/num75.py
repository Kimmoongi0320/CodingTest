# def solution(triangle):
#     n = len(triangle)
#     dp = [[0] * i for i in range(1, n + 1)]
#     # 맨 아랫줄 깊은 복사
#     dp[-1] = triangle[-1][:]

#     for i in range(n - 2, -1, -1):
#         for j in range(i + 1):
#             dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

#     return dp[0][0]


# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))


# 위에서 아래로 내려가는 경우
def solution(triangle):
    n = len(triangle)
    dp = [[0] * i for i in range(1, n + 1)]
    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(i + 1):
            # 첫번째 칸인 경우 윗줄의 첫번째 것만 더할 수 있음
            if j == 0:
                dp[i][j] = dp[i - 1][0] + triangle[i][j]
            # 두번째 칸 부터 마지막 칸 보다 하나 전 칸은 양쪽 칸에서 받을 수 있음
            elif j < i:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
            # 맨 뒷 칸은 맨 윗줄의 맨 마지막 칸만 더할 수 있음
            else:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]

    return max(dp[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
