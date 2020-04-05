from itertools import permutations

def solution(road, n):
    longest = 0

    if n >= road.count("0"):
        return len(road)

    damLocs = list(filter(lambda x: road[x] == "0", range(len(road))))
    combs = list(permutations(damLocs, n))

    for c in combs:
        temp = road
        for i in c:
            temp = temp[:i] + "1" + temp[i+1:]
        if getLongestRoad(temp) > longest:
            longest = getLongestRoad(temp)

    return longest

def getLongestRoad(road):
    roads = road.split("0")
    return len(max(roads))

r1, n1 = "111011110011111011111100011111", 3
r2, n2 = "001100", 5
r3, n3 = "011100", 2

print(solution(r1, n1))
print(solution(r2, n2))
print(solution(r3, n3))

