def solution(words, queries):
    answer = []

    word_map = {}
    for word in words:
        word_length = len(word)
        if word_length not in word_map:
            word_map[word_length] = {}
            word_map[word_length]["first"] = {}
            word_map[word_length]["last"] = {}
        if word[0] not in word_map[word_length]["first"]:
            word_map[word_length]["first"][word[0]] = []
        word_map[word_length]["first"][word[0]].append(word)
        if word[-1] not in word_map[word_length]["last"]:
            word_map[word_length]["last"][word[-1]] = []
        word_map[word_length]["last"][word[-1]].append(word)

    for query in queries:
        cnt = 0
        full_length = len(query)
        comp_in_length = word_map.get(full_length, None)
        if comp_in_length == None:
            answer.append(cnt)
            continue

        split = query.split("?")
        if query[-1] == "?":
            comparatives = comp_in_length["first"].get(query[0], None)
            q = split[0]
        else:
            comparatives = comp_in_length["last"].get(query[-1], None)
            q = split[-1]
        if comparatives == None:
            answer.append(cnt)

        for comparative in comparatives:
            if query[-1] == "?":
                if q == comparative[:len(q)]:
                    cnt += 1
            else:
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
