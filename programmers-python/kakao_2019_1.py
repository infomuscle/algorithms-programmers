def solution(record):
    answer = []
    users = {}
    tempAnswer = []

    for i in range(len(record)):
        cmd = record[i].split()
        try:
            users[cmd[1]] = cmd[2]
        except:
            pass
        tempAnswer.append([cmd[0],cmd[1]])

    for i in range(len(tempAnswer)):
        if tempAnswer[i][0] == "Enter":
            answer.append(users[tempAnswer[i][1]] + "님이 들어왔습니다.")
        elif tempAnswer[i][0] == "Leave":
            answer.append(users[tempAnswer[i][1]] + "님이 나갔습니다.")
        elif tempAnswer[i][0] == "Change":
            pass

    return answer


tc1 = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(tc1))