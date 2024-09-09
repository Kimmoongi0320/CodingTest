from collections import deque


def solution(people: list, limit):
    answer = 0
    people.sort()
    people = deque(people)

    while people:
        # 한명 남은 경우
        if len(people) == 1:
            return answer + 1

        # 제일 무거운 사람과 가벼운 사람
        light = people[0]
        heavy = people[-1]

        if light + heavy <= limit:
            answer += 1
            people.pop()
            people.popleft()
        else:
            answer += 1
            people.pop()
    return answer


print(solution([70, 50, 80, 50], 100))
