from queue import Queue

def solution(bridge_length, weight, truck_weights):
    answer = 0

    waiting_trucks = Queue()
    for tw in truck_weights:
        waiting_trucks.put(tw)

    bridge = Queue()
    last_on_time = 0
    weight_on_bridge = 0

    passed_truck = Queue()

    idx = 0
    while True:
        print(answer, print_queue(bridge), weight_on_bridge, last_on_time)

        if (answer % bridge_length == 0 and answer != 0) or (bridge.qsize() != 0 and last_on_time % bridge_length == 0):
            off_truck = bridge.get()
            passed_truck.put(off_truck)
            weight_on_bridge -= off_truck

        if waiting_trucks.qsize() != 0 and weight_on_bridge + truck_weights[idx] <= weight:
            on_truck = waiting_trucks.get()
            bridge.put(on_truck)
            weight_on_bridge += on_truck
            last_on_time = 0
            idx += 1

        if passed_truck.qsize() == len(truck_weights) and bridge.qsize() == 0:
            break

        answer += 1
        last_on_time += 1
    return answer

def print_queue(queue):
    qList = []
    for i in range(queue.qsize()):
        qList.append(queue.get())
    for q in qList:
        queue.put(q)
    return qList



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
# print(solution(bl2, w2, tw2))
# print(solution(bl3, w3, tw3))
# print(solution(bl4, w4, tw4))
