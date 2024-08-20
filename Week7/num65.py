def solution(s: str):
    change = 0
    zero = 0
    while s != "1":
        zero += s.count("0")
        s = s.replace("0", "")
        # 이진수는 앞에 0b가 붙으므로 제거
        s = bin(len(s))[2:]
        change += 1
    return [change, zero]


print(solution("01110"))
