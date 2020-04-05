def solution(answer_sheet, sheets):
    answer = 0

    while len(sheets) != 0:
        last = sheets.pop()
        for s in sheets:
            temp = getCheatingRate(answer_sheet, last, s)
            if temp > answer:
                answer = temp

    return answer

def getCheatingRate(answer, sheet1, sheet2):
    suspicion = 0
    suspicionLength = 0
    longestSuspicion = 0

    for i in range(len(answer)):
        if answer[i] != sheet1[i] and sheet1[i] == sheet2[i]:
            suspicion += 1
            suspicionLength += 1
        else:
            if suspicionLength > longestSuspicion:
                longestSuspicion = suspicionLength
            suspicionLength = 0

    if suspicionLength > longestSuspicion:
        longestSuspicion = suspicionLength

    return suspicion + (longestSuspicion*longestSuspicion)



as1, s1 = "4132315142", ["3241523133","4121314445","3243523133","4433325251","2412313253"]
as2, s2 = "53241", ["53241", "42133", "53241", "14354"]
as3, s3 = "24551", ["24553", "24553", "24553", "24553"]

print(solution(as1, s1))
print(solution(as2, s2))
print(solution(as3, s3))

# print(getCheatingRate("4132315142", "3241523133", "3243523133"))
# print(getCheatingRate("24551", "24553", "24553"))