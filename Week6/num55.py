from collections import deque


def solution(arr1, arr2):
    total_length = len(arr1) + len(arr2)
    arr1 = deque(arr1)
    arr2 = deque(arr2)
    answer = []
    for i in range(total_length):
        if arr1 and arr2:
            if arr1[0] > arr2[0]:
                answer.append(arr2[0])
                arr2.popleft()
            else:
                answer.append(arr1[0])
                arr1.popleft()
        elif not arr1:
            answer.extend(list(arr2))
            break
        else:
            answer.extend(list(arr1))
            break
    return answer


print(solution([1, 3, 5], [2, 4, 6]))
print(solution([1, 2, 3], [4, 5, 6]))
