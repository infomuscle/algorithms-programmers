from queue import PriorityQueue
from queue import Queue


def solution(jobs):
    answer = 0
    proc_times = []

    jobs = sorted(jobs, key=lambda x: x[0])
    processor = Queue()
    requests = PriorityQueue()
    time = 0
    idx = 0
    while True:
        # print(time)
        if jobs[idx][0] == time:
            requests.put((jobs[idx][1], jobs[idx]))
            if idx < len(jobs) - 1:
                idx += 1

        if processor.qsize() != 0:
            job = processor.get()
            # print(job)
            if time - job[0] == job[1][1]:
                # proc_times.append([job[0], time])
                # proc_times.append([job[1][0], time])
                proc_times.append(time - job[1][0])
            else:
                processor.put(job)

        if processor.qsize() == 0 and requests.qsize() != 0:
            request = requests.get()
            processor.put([time, request[1]])

        if idx == len(jobs) - 1 and processor.qsize() == 0:
            break

        time += 1

    # print(proc_times)
    answer = int(sum(proc_times) / len(proc_times))
    return answer


j1 = [[0, 3], [1, 9], [2, 6]]
j2 = [[0, 3], [2, 6], [1, 9]]

print(solution(j1))
print(solution(j2))
