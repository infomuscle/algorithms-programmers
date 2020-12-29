def solution(m, musicinfos):
    melody = convert_chords(m)
    # print("melody:", melody)

    musics = []
    for i, musicinfo_str in enumerate(musicinfos):
        music_info = musicinfo_str.split(",")
        play_time = get_play_time(music_info[0], music_info[1])
        sheet = convert_chords(music_info[3])
        played_chords = sheet * (play_time // len(sheet) + 1)
        played_chords = played_chords[:play_time]
        # print("played_chords:", played_chords)

        for j in range(len(played_chords)):
            if played_chords[j:j + len(melody)] == melody:
                # print(played_chords[j:j + len(melody)])
                musics.append((music_info[2], play_time, i))
                break
    # print("musics:", musics)

    if len(musics) == 0:
        return "(None)"
    if len(musics) == 1:
        return musics[0][0]
    musics = sorted(musics, key=lambda x: (-x[1], x[2]))

    return musics[0][0]


def get_play_time(start_time, end_time):
    start_info = list(map(int, start_time.split(":")))
    end_info = list(map(int, end_time.split(":")))

    play_time = (end_info[0] * 60 + end_info[1]) - (start_info[0] * 60 - start_info[1])

    return play_time


def convert_chords(chords: str):
    converted = []

    stack = []
    for chord in chords:
        if chord == "#" or len(stack) == 0:
            stack.append(chord)
            continue
        else:
            tmp = ""
            while len(stack) > 0:
                tmp += stack.pop()
            converted.append(tmp[::-1])
            stack.append(chord)
    if len(stack) > 0:
        tmp = ""
        while len(stack) > 0:
            tmp += stack.pop()
        converted.append(tmp[::-1])

    return converted


m1 = "ABCDEFG"
mi1 = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
m2 = "CC#BCC#BCC#BCC#B"
mi2 = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
m3 = "ABC"
mi3 = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

print(solution(m1, mi1))
print(solution(m2, mi2))
print(solution(m3, mi3))

# chords = music_info[3] * (play_time // len(music_info[3]) + 1)
# chords = chords[:play_time]
# if m in chords:
#     musics.append((music_info[2], play_time, i))
