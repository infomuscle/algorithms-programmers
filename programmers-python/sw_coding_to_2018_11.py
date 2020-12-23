def solution(n, words):
    answer = []

    words_by_person = dict()
    words_spoken = dict()

    last_word = words[0][0]
    for i, word in enumerate(words):
        person = i % n + 1
        if person not in words_by_person:
            words_by_person[person] = list()

        if word not in words_spoken and word[0] == last_word[-1]:
            words_spoken[word] = True
            words_by_person[person].append(word)
        else:
            answer.append(person)
            answer.append(len(words_by_person[person]) + 1)
            break

        last_word = word

        if i + 1 == len(words):
            return [0, 0]

    return answer


n1 = 3
w1 = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
n2 = 5
w2 = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
n3 = 2
w3 = ["hello", "one", "even", "never", "now", "world", "for"]

print(solution(n1, w1))
print(solution(n2, w2))
print(solution(n3, w3))
