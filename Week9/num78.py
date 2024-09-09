def solution(board):
    dp = [[0] * len(board[0]) for _ in range(len(board))]
    dp[0] = board[0][:]
    for i in range(1, len(board)):
        dp[i][0] = board[i][0]

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    # return max(max(dp)) 를 하게 되면 첫번째 인자를 비교해서 최대값인 리스트를 리턴 함(사전식)
    # ex) [3,2,1] > [1,5436,3123]
    return max(max(row) for row in dp) ** 2


print(solution([[0, 0], [0, 0]]))
