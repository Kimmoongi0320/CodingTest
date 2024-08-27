def solution(topping):
    answer = 0

    # 형의 토핑 개수 저장
    brother_topping = []
    brother_topping_count = set()

    # 동생 토핑 개수 저장
    sister_topping = []
    sister_topping_count = set()

    # 형 토핑 계산
    for t in topping:
        brother_topping_count.add(t)
        brother_topping.append(len(brother_topping_count))

    # 동생 토핑 계산
    for t in reversed(topping):
        sister_topping_count.add(t)
        sister_topping.append(len(sister_topping_count))

    # 다시 리스트 뒤집기
    sister_topping.reverse()

    # 두 배열을 비교하여 토핑의 수가 같은 경우 answer+=1
    for i in range(1, len(topping)):
        if brother_topping[i - 1] == sister_topping[i]:
            answer += 1

    return answer


"""
이렇게 slicing을 사용 할 경우 각각 O(i),O(n-i) 만큼의 시간 복잡도가 소요된다.(슬리이싱은 새 리스트를 생성하기 때문)
따라서 for문도 돌고 있으므로 최대 O(N^2)의 시간이 소요되게됨.

def solution(topping):
    answer = 0
    for i in range(1, len(topping)):
        topping1 = topping[:i]
        topping2 = topping[i:]
        if len(set(topping1)) == len(set(topping2)):
            answer += 1
    return answer

"""
print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
