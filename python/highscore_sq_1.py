def solution(bridge_length, weight, truck_weights):
    answer = 0

    truck_cnt = len(truck_weights)

    pl, pr = 0, 1
    cnt = 0
    while pl < truck_cnt:
        cnt += 1
        while sum(truck_weights[pl:pr]) <= weight and pr < len(truck_weights):
            pr += 1
            if sum(truck_weights[pl:pr]) > weight:
                pr -= 1
                break
        answer += bridge_length + pr - pl
        pl = pr
        pr = pl + 1

    answer -= cnt - 1

    return answer


bl1 = 2
w1 = 10
tw1 = [7, 4, 5, 6]

bl2 = 100
w2 = 100
tw2 = [10]

bl3 = 100
w3 = 100
tw3 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

bl4 = 1
w4 = 10
tw4 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

print(solution(bl1, w1, tw1))
print(solution(bl2, w2, tw2))
print(solution(bl3, w3, tw3))
print(solution(bl4, w4, tw4))
