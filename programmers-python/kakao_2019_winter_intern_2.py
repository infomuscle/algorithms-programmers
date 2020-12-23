def solution(s):
    answer = []

    s_list = []
    tmp = ""
    for i in range(1, len(s) - 1):
        if s[i] == "{":
            tmp = ""
        elif s[i] == "}":
            s_list.append(tmp.split(","))
        else:
            tmp += s[i]

    max = 0
    for i in range(len(s_list)):
        if len(s_list[i]) > max:
            max = len(s_list[i])

    cnt = 1
    idx = 0
    while len(answer) != max:
        for i in range(len(s_list)):
            if cnt == len(s_list[i]):
                for ch in s_list[i]:
                    if int(ch) not in answer:
                        answer.append(int(ch))
                        cnt += 1
                        idx += 1
                        break

    return answer


s1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s3 = "{{20,111},{111}}"
s4 = "{{123}}"
s5 = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
print(solution(s5))
