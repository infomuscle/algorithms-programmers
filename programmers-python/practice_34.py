def solution(s):
    nums = sorted(list(map(int, s.split(" "))))

    answer = str(nums[0]) + " " + str(nums[-1])

    return answer


s1 = "1 2 3 4"
s2 = "-1 -2 -3 -4"
s3 = "-1 -1"

print(solution(s1))
print(solution(s2))
print(solution(s3))
