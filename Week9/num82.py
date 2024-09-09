def solution(d: list, budget):
    d.sort()

    answer = 0
    current = 0
    while budget > 0:
        if current == len(d) or d[current] > budget:
            return answer
        else:
            budget -= d[current]
            current += 1
            answer += 1

    return answer


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))
