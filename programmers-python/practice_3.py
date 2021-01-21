import datetime


def solution(a, b):
    d = datetime.datetime(2016, a, b)
    return d.strftime('%A')[:3].upper()


print(solution(5, 24))
