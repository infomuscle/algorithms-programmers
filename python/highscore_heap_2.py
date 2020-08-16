import heapq
from queue import Queue


def solution(jobs):
    # 정렬 필수
    jobs = sorted(jobs, key=lambda x: x[0])

    proc_times = []
    processor = Queue()
    requests = []
    time, idx = 0, 0
    while True:
        if jobs[idx][0] == time:
            heapq.heappush(requests, (jobs[idx][1], jobs[idx]))
            if idx < len(jobs) - 1:
                idx += 1

        if processor.qsize() != 0:
            job = processor.get()
            if time - job[0] == job[1][1]:
                proc_times.append(time - job[1][0])
            else:
                processor.put(job)

        if processor.qsize() == 0 and len(requests) != 0:
            request = heapq.heappop(requests)
            processor.put([time, request[1]])

        if idx == len(jobs) - 1 and processor.qsize() == 0:
            break

        time += 1

    answer = int(sum(proc_times) / len(proc_times))
    return answer


j1 = [[0, 3], [1, 9], [2, 6]]
j2 = [[0, 3], [2, 6], [1, 9]]

print(solution(j1))
print(solution(j2))
