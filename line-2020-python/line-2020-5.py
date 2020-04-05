import operator

def solution(dataSource, tags):
    answer = []
    scoreMap = {}

    for d in dataSource:
        scoreMap[d[0]] = 0

    for t in tags:
        for d in dataSource:
            if t in d:
                scoreMap[d[0]] += 1

    sList = sorted(scoreMap.items(), key=operator.itemgetter(1), reverse=True)
    for l in sList:
        if l[1] != 0:
            answer.append(l[0])
    print(sList)

    return answer[:10]

ds1 = [
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
]
t1 = ["t1", "t2", "t3"]

ds2 = [
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"],
    ["doc6", "t1", "t4", "t8"],
    ["doc7", "t2", "t5", "t8"],
    ["doc8", "t6", "t7", "t8"],
    ["doc9", "t6", "1", "t8"],
    ["doc10", "t6", "t2", "t8", "t1", "t3"],
    ["doc11", "t6", "t2", "t8", "t1", "t3"]
]
t2 = ["t1", "t2", "t3", "t8"]

# print(solution(ds1, t1))
print(solution(ds2, t2))