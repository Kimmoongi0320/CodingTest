def solution(numbers):
    numbers = [str(num) for num in numbers]
    numbers = sorted(numbers, key=lambda x: x * 3, reverse=True)
    print(numbers)

    answer = ""
    for num in numbers:
        answer += num
    # 전부 0인 경우
    if answer[0] == "0":
        answer = "0"
    return answer


print(solution([3, 300, 31]))
