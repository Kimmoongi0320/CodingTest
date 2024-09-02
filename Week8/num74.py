def solution(n):
    dp = [1, 2, 3, 5]
    # 기본 저장되어 있는 인덱스가 주어지면 바로 반환
    if n <= 4:
        return dp[n - 1]
    for i in range(4, n + 1):
        dp.append((dp[i - 1] + dp[i - 2]) % 1000000007)
    return dp[n - 1]


print(solution(1))
