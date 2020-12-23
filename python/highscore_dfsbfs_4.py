def solution(tickets):
    answer = []

    ticket_map = dict()
    for ticket in tickets:
        if ticket[0] not in ticket_map:
            ticket_map[ticket[0]] = set()
        ticket_map[ticket[0]].add(tuple(ticket))

    used_tickets = []
    stack = sorted(list(ticket_map["ICN"]), reverse=True)
    while stack:
        node = stack.pop()
        if node not in used_tickets:
            if node[1] in ticket_map:
                used_tickets.append(node)
                stack.extend(sorted(list(ticket_map[node[1]] - set(used_tickets)), reverse=True))
            elif len(used_tickets) == len(tickets) - 1:
                used_tickets.append(node)
                break

    answer.append("ICN")
    for used_ticket in used_tickets:
        answer.append(used_ticket[1])

    return answer


t1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
t2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
t3 = [["ICN", "SFO"], ["SFO", "ATL"], ["SFO", "JFK"], ["JFK", "SFO"]]  # ICN - SFO - JFK - SFO - ATL
t4 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "JFK"], ["JFK", "ICN"]]  # ICN - SFO - JFK - ICN - ATL

# print(solution(t1))
# print(solution(t2))
# print(solution(t3))
print(solution(t4))
