def solution(nums):
    dp = [0] * len(nums)
    # 첫번째 숫자는 무조건 1
    dp[0] = 1

    for i in range(1, len(nums)):
        for j in range(i - 1, -1, -1):
            # 이전 숫자가 현재 숫자보다 작고 dp값은 이전 숫자보다 작은경우 교체
            if nums[j] < nums[i] and dp[j] > dp[i]:
                dp[i] = dp[j]
        # 위 조건을 만족하는 최대값에서 1 더해주기
        dp[i] += 1
    return max(dp)


print(solution([1, 3, 2, 3, 1, 5, 7, 3]))
print(solution([3, 2, 1]))
