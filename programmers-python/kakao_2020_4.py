def solution(words, queries):
    answer = []

    word_map = {}
    for word in words:
        if len(word) not in word_map:
            word_map[len(word)] = []
        word_map[len(word)].append(word)

    for query in queries:
        cnt = 0
        full_length = len(query)
        comparatives = word_map.get(full_length, None)
        if comparatives == None:
            answer.append(cnt)
            continue
        split = query.split("?")
        for comparative in comparatives:
            if query[-1] == "?":
                q = split[0]
                if q == comparative[:len(q)]:
                    cnt += 1
            else:
                q = split[-1]
                if q == comparative[full_length - len(q):]:
                    cnt += 1
        answer.append(cnt)

    return answer


w1 = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
q1 = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(w1, q1))
# query_map = {}
# for i, query in enumerate(queries):
#     tmp = {}
#     tmp["string"] = query
#     tmp["full_length"] = len(query)
#     tmp["wc_length"] = query.count("?")
#     if query[0] == "?":
#         tmp["type"] = "prefix"
#     else:
#         tmp["type"] = "suffix"
#     query_map[i] = tmp
