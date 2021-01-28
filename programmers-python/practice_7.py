def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return "김서방은 " + str(i) + "에 있다"


s1 = ["Jane", "Kim"]
print(solution(s1))
