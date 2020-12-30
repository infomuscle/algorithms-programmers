def solution(nums):
    allowed = len(nums) // 2

    mine = {}
    for num in nums:
        if num not in mine:
            mine[num] = True
        if len(mine) == allowed:
            break

    return len(mine)


n1 = [3, 1, 2, 3]
n2 = [3, 3, 3, 2, 2, 4]
n3 = [3, 3, 3, 2, 2, 2]

print(solution(n1))
print(solution(n2))
print(solution(n3))
