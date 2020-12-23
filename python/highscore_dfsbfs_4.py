def solution(tickets):
    answer = []

    ticket_map = dict()
    for i, ticket in enumerate(tickets):
        if ticket[0] not in ticket_map:
            ticket_map[ticket[0]] = set()
        ticket.append(i)
        ticket_map[ticket[0]].add(tuple(ticket))
    # print(ticket_map)

    used_tickets = []
    stack = sorted(list(ticket_map["ICN"]), reverse=True)
    while stack:
        ticket = stack.pop()
        if ticket not in used_tickets:
            arrival = ticket[1]
            if arrival in ticket_map:
                used_tickets.append(ticket)
                stack.extend(sorted(list(ticket_map[arrival] - set(used_tickets)), reverse=True))
            elif len(used_tickets) == len(tickets) - 1:
                used_tickets.append(ticket)
                break

    answer.append("ICN")
    for used_ticket in used_tickets:
        answer.append(used_ticket[1])

    return answer


t1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]  # ICN - JFK - HND - IAD
t2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]  # ICN - ATL - ICN - SFO - ATL -SFO
t3 = [["ICN", "SFO"], ["SFO", "ATL"], ["SFO", "JFK"], ["JFK", "SFO"]]  # ICN - SFO - JFK - SFO - ATL
t4 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "JFK"], ["JFK", "ICN"]]  # ICN - SFO - JFK - ICN - ATL
t5 = [["ICN", "HND"], ["ICN", "SFO"], ["ICN", "JFK"], ["JFK", "ICN"], ["HND", "ICN"]]  # ICN - HND - ICN - JFK - ICN - SFO
t6 = [["ICN", "JFK"], ["JFK", "ATL"], ["JFK", "IAD"], ["IAD", "HND"], ["HND", "JFK"]]  # ICN - JFK - IAD - HND - JFK - ATL
t7 = [["ICN", "JFK"], ["JFK", "ICN"], ["ICN", "JFK"], ["JFK", "ICN"]]  # ICN - JFK - ICN - JFK - ICN

print(solution(t1))
print(solution(t2))
print(solution(t3))
print(solution(t4))
print(solution(t5))
print(solution(t6))
print(solution(t7))
