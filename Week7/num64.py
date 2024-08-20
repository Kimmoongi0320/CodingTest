def solution(n):
    answer = [[0] * n for _ in range(n)]
    num = 1
    # 첫번째 줄 채우기
    for i in range(n):
        answer[0][i] = num
        num += 1
    x, y = 0, n - 1
    plus = False
    for j in range(n - 1, 0, -1):
        if not plus:
            for _ in range(j):
                x += 1
                answer[x][y] = num
                num += 1
            for _ in range(j):
                y -= 1
                answer[x][y] = num
                num += 1
            plus = True
        else:
            for _ in range(j):
                x -= 1
                answer[x][y] = num
                num += 1
            for _ in range(j):
                y += 1
                answer[x][y] = num
                num += 1
            plus = False
    return answer


print(solution(3))
print(solution(4))
