def solution(tickets):
    answer = []

    ticket_map = dict()
    for ticket in tickets:
        if ticket[0] not in ticket_map:
            ticket_map[ticket[0]] = set()
        ticket_map[ticket[0]].add(tuple(ticket))

    used_tickets = []
    stack = [sorted(list(ticket_map["ICN"]))[0]]
    while stack:
        node = stack.pop()
        if node not in used_tickets:
            used_tickets.append(node)
            if len(used_tickets) == len(tickets):
                break
            stack.extend(sorted(list(ticket_map[node[1]] - set(used_tickets)), reverse=True))

    answer.append("ICN")
    for used_ticket in used_tickets:
        answer.append(used_ticket[1])

    return answer


t1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
t2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

print(solution(t1))
print(solution(t2))
