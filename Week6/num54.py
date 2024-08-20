def solution(s):
    word_list = [0] * 26
    answer = ""
    for cha in s:
        word_list[ord(cha) - ord("a")] += 1

    for i in range(len(word_list)):
        times = word_list[i]
        answer += chr(i + ord("a")) * times
    return answer


print(solution("hello"))
