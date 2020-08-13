from queue import PriorityQueue


def solution(scoville, K):
    answer = 0

    pq = PriorityQueue()
    for s in scoville:
        pq.put(s)

    while pq.qsize() > 1:
        answer += 1
        mix = pq.get() + pq.get() * 2
        pq.put(mix)

        least = pq.get()
        if least > K:
            break
        else:
            pq.put(least)

    if pq.qsize() == 1 and pq.get() < K:
        answer = -1

    return answer


s1 = [1, 2, 3, 9, 10, 12]
k1 = 7
print(solution(s1, k1))
