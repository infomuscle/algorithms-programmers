def solution(words, queries):
    answer = []

    trie = {}
    trie_rev = {}
    for word in words:
        word_length = len(word)

        if word_length not in trie:
            trie[word_length] = [0, {}]
        trie[word_length][0] += 1

        node = trie[word_length][1]
        for w in word:
            if w not in node:
                node[w] = [0, {}]
            node[w][0] += 1
            node = node[w][1]

        word = word[::-1]

        if word_length not in trie_rev:
            trie_rev[word_length] = [0, {}]
        trie_rev[word_length][0] += 1

        node = trie_rev[word_length][1]
        for w in word:
            if w not in node:
                node[w] = [0, {}]
            node[w][0] += 1
            node = node[w][1]

    for query in queries:
        query_length = len(query)
        if query_length not in trie:
            answer.append(0)
            continue

        if query[0] != "?":
            node = trie[query_length]
        else:
            node = trie_rev[query_length]
            query = query[::-1]

        for q in query:
            if q != "?":
                node = node[1].get(q, None)
                if node == None:
                    answer.append(0)
                    break
                continue
            else:
                answer.append(node[0])
                break

    return answer


w1 = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
q1 = ["fro??", "????o", "fr???", "fro???", "pro?"]

w2 = ["t", "o"]
q2 = ["?"]

print(solution(w1, q1))
print(solution(w2, q2))
