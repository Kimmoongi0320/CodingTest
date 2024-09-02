# 가중치 배열 생성 해야됨
def solution(arr):
    dp = [[0] * len(arr[0]) for _ in range(4)]
    # 첫 줄 가중치 초기화
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[2][0] = arr[2][0]
    dp[3][0] = arr[0][0] + arr[2][0]

    for i in range(1, len(arr[0])):
        # 상단 줄 고를 경우 이전 줄은 중단or하단 중에 큰 값
        dp[0][i] = arr[0][i] + max(dp[1][i - 1], dp[2][i - 1])
        # 중간 줄 고를 경우 이전 줄의 상단 or 하단 or 상하단 합 중에 큰 값
        dp[1][i] = arr[1][i] + max(dp[0][i - 1], dp[2][i - 1], dp[3][i - 1])
        # 하단 줄 고를 경우
        dp[2][i] = arr[2][i] + max(dp[0][i - 1], dp[1][i - 1])
        # 상하단 줄 고를 경우
        dp[3][i] = arr[0][i] + arr[2][i] + dp[1][i - 1]

    return max(dp[0][-1], dp[1][-1], dp[2][-1], dp[3][-1])


print(solution([[1, 3, 3, 2], [2, 1, 4, 1], [1, 5, 2, 3]]))
