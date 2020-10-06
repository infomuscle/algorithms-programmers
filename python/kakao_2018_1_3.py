import operator


def solution(cacheSize, cities):
    answer = 0

    cache = {}

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        if city not in cache and len(cache) < cacheSize:
            cache[city] = 1
            answer += 5
        elif city not in cache and len(cache) >= cacheSize:
            cache_sorted = sorted(cache.items(), key=operator.itemgetter(1))
            del cache[cache_sorted[0][0]]
            cache[city] = 1
            answer += 5
        elif city in cache:
            cache[city] += 1
            answer += 1

    return answer


cs1 = 3
ct1 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cs2 = 3
ct2 = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
cs3 = 2
ct3 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
cs4 = 5
ct4 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
cs5 = 2
ct5 = ["Jeju", "Pangyo", "NewYork", "newyork"]
cs6 = 0
ct6 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cs7 = 1
ct7 = ["Jeju", "Jeju", "Pangyo", "Pangyo", "Jeju"]

print(solution(cs1, ct1))
print(solution(cs2, ct2))
print(solution(cs3, ct3))
print(solution(cs4, ct4))
print(solution(cs5, ct5))
print(solution(cs6, ct6))
print(solution(cs7, ct7))
