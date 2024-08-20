def solution(n):
    # 문자열 sorted 하면 리스트로 변환 String.sort()는 불가능
    num = "".join(sorted(str(n), reverse=True))
    return int(num)
