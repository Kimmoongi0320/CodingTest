def solution(blue, white):
    # 약수 탐색 하기 위해 제곱근 사용
    for i in range(1, int(white**0.5) + 1):
        if white % i == 0:
            # 가로 값
            side = white // i
            # (가로 + 세로) *2 + 4(각 모서리) == 파랑색 개수
            if (side + i) * 2 + 4 == blue:
                return [side + 2, i + 2]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
