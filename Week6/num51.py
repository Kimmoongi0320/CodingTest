score_board = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def calculate_score(info, shoot):
    total = len(info)
    diff_score = 0
    for i in range(total):
        if info[i] == 0 and shoot[i] == 0:
            continue
        elif info[i] < shoot[i]:
            diff_score += score_board[i]
        else:
            diff_score -= score_board[i]
    return diff_score


def solution(n, info):
    result = [-1]
    # 최대 점수 차이
    max_diff_score = [0]
    # 점수 별 자신이 맞춘 화살
    shoot = [0] * 11

    def back_tracking(bullet, info, shoot, startpoint):
        # 화살이 남아있는 경우 0점에 화살 개수를 더해주고 점수 계산
        if bullet > 0 and startpoint < 0:
            shoot[-1] += bullet
            score = calculate_score(info, shoot)
            if max_diff_score[0] < score:
                # 최대 점수 차이 바꿔 주고 result값 바꿔 주기
                max_diff_score[0] = score
                result[:] = shoot[:]
            shoot[-1] -= bullet
            return
        elif bullet == 0:
            # 점수 차이 계산
            score = calculate_score(info, shoot)
            if max_diff_score[0] < score:
                # 최대 점수 차이 바꿔 주고 result값 바꿔 주기
                max_diff_score[0] = score
                result[:] = shoot[:]
            return
        # 적은 점수 많이 맞춰야 함으로 낮은 점수부터 보기
        for i in range(startpoint, -1, -1):
            # 적은 점수를 많이 쏴야 하므로 0점은 상대보다 한발 적게 나머지는 상대보다 한발 많이 쏴야 함
            will_shoot = (info[i] - 1) if i == 10 and info[i] >= 1 else (info[i] + 1)

            shoot[i] = will_shoot
            back_tracking(bullet - will_shoot, info, shoot, i - 1)
            shoot[i] = 0

    back_tracking(n, info, shoot, 10)
    # 점수 갱신이 안되었을 경우
    if max_diff_score[0] == 0:
        return [-1]
    else:
        return result
