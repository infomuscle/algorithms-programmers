def solution(record):
    answer = []
    chattersIn = {}
    chattersOut = {}
    
    for i in range(len(record)):
        cmd = list(record[i].split())
        if cmd[0] == "Enter":
            chattersIn[cmd[1]] = cmd[2]
        elif cmd[0] == "Change":
            chattersIn[cmd[1]] = cmd[2]
        elif cmd[0] == "Leave":
            chattersOut[cmd[1]] = chattersIn[cmd[1]]
            del chattersIn[cmd[1]]

    for i in range(len(record)):
        cmd = list(record[i].split())
        if cmd[0] == "Enter":
            if cmd[1] in chattersIn:
                answer.append("{0}님이 들어왔습니다.".format(chattersIn[cmd[1]]))
            else:
                answer.append("{0}님이 들어왔습니다.".format(chattersOut[cmd[1]]))
        elif cmd[0] == "Leave":
            if cmd[1] in chattersIn:
                answer.append("{0}님이 나갔습니다.".format(chattersIn[cmd[1]]))
            else:
                answer.append("{0}님이 나갔습니다.".format(chattersOut[cmd[1]]))
    return answer

record1 = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
record2 = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan", "Enter uid2345 Neo"]
record3 = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan", "Enter uid2345 Neo", "Change uid1234 Neo", "Change uid4567 Neo"]
record4 = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan", "Enter uid2345 Neo", "Change uid1234 Neo", "Change uid4567 Neo", "Leave uid1234", "Leave uid4567", "Leave uid2345"]

print(solution(record1))
print(solution(record2))
print(solution(record3))
print(solution(record4))