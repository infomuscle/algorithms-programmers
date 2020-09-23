def solution(n, lost, reserve):
    answer = 0

    reserve_tmp = []
    for r in reserve:
        if r not in lost:
            reserve_tmp.append(r)
    reserve = reserve_tmp


    can_borrow = 0
    for l in lost:
        if l + 1 in reserve or l - 1 in reserve:
            can_borrow += 1
    # 앞에를 가져가야 하나 뒤에를 가져가야 하나

    answer = n - len(lost) + can_borrow

    return answer


n1 = 5
l1 = [2, 4]
r1 = [1, 3, 5]
n2 = 5
l2 = [2, 4]
r2 = [3]
n3 = 3
l3 = [3]
r3 = [1]

print(solution(n1, l1, r1))
print(solution(n2, l2, r2))
print(solution(n3, l3, r3))
