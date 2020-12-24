def solution(words, queries):
    answer = []

    word_map = {}
    for word in words:
        if len(word) not in word_map:
            word_map[len(word)] = []
        word_map[len(word)].append(word)
    # print(word_map)

    query_map = {}
    for i, query in enumerate(queries):
        tmp = {}
        tmp["string"] = query
        tmp["full_length"] = len(query)
        tmp["wc_length"] = query.count("?")
        if query[0] == "?":
            tmp["type"] = "prefix"
        else:
            tmp["type"] = "suffix"
        query_map[i] = tmp
    # print(query_map)

    for key in query_map:
        cnt = 0
        query_info = query_map[key]
        comparatives = word_map.get(query_info["full_length"], None)
        if comparatives == None:
            answer.append(cnt)
            continue
        for comparative in comparatives:
            if query_info["type"] == "suffix":
                q = query_info["string"].split("?")[0]
                if q == comparative[:len(q)]:
                    cnt += 1
            else:
                q = query_info["string"].split("?")[-1]
                if q == comparative[query_info["full_length"] - len(q):]:
                    cnt += 1

        answer.append(cnt)

    return answer


w1 = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
q1 = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(w1, q1))
