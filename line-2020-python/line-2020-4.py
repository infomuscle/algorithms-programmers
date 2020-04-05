def solution(snapshots, transactions):
    tMap = {}
    aMap = {}
    answer = []

    for a in snapshots:
        aMap[a[0]] = int(a[1])

    for t in transactions:
        if t[0] not in tMap:
            tMap[t[0]] = t[1:]

    for v in tMap.values():
        if v[0] == "SAVE":
            if v[1] in aMap:
                aMap[v[1]] += int(v[2])
            else:
                aMap[v[1]] = int(v[2])
        else:
            if v[1] in aMap:
                aMap[v[1]] -= int(v[2])
            # else:
            #     aMap[v[1]] = -int(v[2]) # 계좌 없는데 인출 가능?

    for k in aMap.keys():
        answer.append([k, str(aMap[k])])

    answer = sorted(answer)

    return answer

s1 = [
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"]
]

t1 = [
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]

s2 = [
    ["ACCOUNT3", "200"],
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"]
]

t2 = [
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"],
  ["5", "WITHDRAW", "ACCOUNT4", "30"]
]

print(solution(s1, t1))
print(solution(s2, t2))