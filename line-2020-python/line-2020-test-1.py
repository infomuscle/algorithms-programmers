def solution(v):
    answer = []
    mapX = {}
    mapY = {}

    for x in v:
        try:
            mapX[x[0]] += 1
        except:
            mapX[x[0]] = 1
        try:
            mapY[x[1]] += 1
        except:
            mapY[x[1]] = 1

    for k in mapX.keys():
        if mapX[k] == 1:
            answer.append(k)
    for k in mapY.keys():
        if mapY[k] == 1:
            answer.append(k)

    return answer

