def solution(items, weight_limit):
    # [무게 당 가치, 해당 가치의 상품 idx] 형태
    values = [[round(item[1] / item[0], 2), idx] for idx, item in enumerate(items)]
    # 가치 높은 순으로 정렬
    values.sort(reverse=True)
    answer = 0
    # 현재 가치 idx
    current_value_idx = 0
    while weight_limit > 0:
        # 만약 현재 가치에 해당하는 상품이 없는 경우 다음 가치로 넘어가기
        if items[values[current_value_idx][1]][0] == 0:
            current_value_idx += 1
            # 만약 물건을 전부 사용 한경우 정답 리턴
            if current_value_idx >= len(items):
                return answer
        # 현재 가치 할당
        current_value = values[current_value_idx][0]

        # 정답에 현재가치 더해주기
        answer += current_value
        # 해당 가치의 상품 1개 줄여주기
        items[values[current_value_idx][1]][0] -= 1
        # 무게 1 감소
        weight_limit -= 1
    return answer


print(solution([[10, 60], [20, 100], [30, 120]], 50))
