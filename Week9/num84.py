from collections import defaultdict


def solution(k, tangerine):
    result = 0
    fruit_dict = defaultdict(int)
    tangerine.sort()

    for fruit in tangerine:
        fruit_dict[str(fruit)] += 1

    fruit_kinds = sorted(fruit_dict.items(), key=lambda x: x[1], reverse=True)
    total = 0
    for big in fruit_kinds:
        total += big[1]
        result += 1

        if total >= k:
            return result

    return result


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
