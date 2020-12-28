from itertools import combinations


def solution(relation):
    answer = 0

    col_size = len(relation[0])
    col_combs = []
    for i in range(col_size):
        col_combs.extend(list(combinations([x for x in range(col_size)], i + 1)))

    pk_cols = []
    for col_comb in col_combs:
        key_map = {}
        is_key_repeat = False
        for row in relation:
            key = "".join([row[col] for col in col_comb])
            if key in key_map:
                is_key_repeat = True
                break
            else:
                key_map[key] = True
        if is_key_repeat:
            continue

        is_key_minium = True
        for pk_col in pk_cols:
            if len(set(pk_col) - set(col_comb)) == 0:
                is_key_minium = False
                break
        if is_key_minium:
            pk_cols.append(col_comb)
            answer += 1

    return answer


r1 = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
print(solution(r1))
