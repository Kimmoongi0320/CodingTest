def moiving(key, current, max_x, max_y):
    if key == "left":
        if current[0] - 1 < max_x * -1:
            return current
        current[0] -= 1
        return current
    elif key == "right":
        if current[0] + 1 > max_x:
            return current
        current[0] += 1
        return current
    elif key == "up":
        if current[1] + 1 > max_y:
            return current
        current[1] += 1
        return current
    else:
        if current[1] - 1 < max_y * -1:
            return current
        current[1] -= 1
        return current


def solution(keyinput, board):
    current = [0, 0]
    max_x = (board[0] - 1) // 2
    max_y = (board[1] - 1) // 2

    for key in keyinput:
        current = moiving(key, current, max_x, max_y)
    return current


print(solution(["left", "right", "up", "right", "right"], [11, 11]))
