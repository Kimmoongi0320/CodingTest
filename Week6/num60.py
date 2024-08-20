def solution(s):
    num_list = s[2:-2].split("},{")
    num_list = sorted(num_list, key=len)
    answer = []
    answer.append(int(num_list[0]))
    for total in num_list[1:]:
        numbers = total.split(",")
        for num in numbers:
            if int(num) not in answer:
                answer.append(int(num))
    return answer


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
