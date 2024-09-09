def solution(land):
    n = len(land)
    dp = [[0] * len(land[0]) for _ in range(n)]
    dp[0] = land[0][:]

    for i in range(1, n):
        # 이전 줄 최대값
        last_max = max(dp[i - 1])
        # 최대값의 인덱스 값
        max_idx = dp[i - 1].index(last_max)
        for j in range(4):
            # 같은줄에 없을경우
            if max_idx != j:
                dp[i][j] = last_max + land[i][j]
            # 같은 줄일 경우 해당 인덱스 제외 최댓값을 더해줌
            else:
                new_list = [val for i, val in enumerate(dp[i - 1]) if i != max_idx]
                dp[i][j] = max(new_list) + land[i][j]

    return max(dp[-1])


print(solution([[6, 7, 1, 2], [2, 3, 10, 8], [1, 3, 9, 4], [7, 11, 4, 9]]))
