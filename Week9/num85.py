def solution(n, stations, w):
    # 기지국이 커버하는 첫 구간의 끝
    last_end = 1
    answer = 0
    coverage = 2 * w + 1

    for station in stations:
        start = station - w
        end = station + w

        # 기지국이 커버하지 않는 구간의 길이 계산
        if start > last_end:
            remain_range = start - last_end
            # 필요한 기지국 개수 계산
            answer += (remain_range + coverage - 1) // coverage

        # 다음 기지국이 커버하지 않는 구간의 시작 설정
        last_end = end + 1

    # 마지막 기지국이 커버하지 않는 구간 처리
    if last_end <= n:
        remain_range = n - last_end + 1
        answer += (remain_range + coverage - 1) // coverage

    return answer


print(solution(16, [9], 2))
