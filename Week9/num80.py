def solution(amount):
    money_list = [1, 10, 50, 100]
    idx = 3
    answer = []

    money = money_list[idx]
    while amount > 0:
        # 선택 금액이 총 금액보다 작아질때 까지 감소
        while amount < money:
            idx -= 1
            money = money_list[idx]
        amount -= money
        answer.append(money)
    return answer


print(solution(123))
print(solution(350))
