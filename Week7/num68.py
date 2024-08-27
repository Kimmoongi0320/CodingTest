def solution(n):
    result = 0
    num = n
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
            result += 1
    return result + 1


""" 시바 개싸가지 없네 정답
def solution(n):
    return bin(n).count("1")
"""

print(solution(5))
print(solution(6))
print(solution(5000))
