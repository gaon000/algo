def solution(genres, plays):
    from collections import defaultdict
    count = 0
    answer = []
    gen_play_list = []
    gen_play = defaultdict(int)
    for i in range(len(genres)):
        gen_play[genres[i]] += plays[i]
        gen_play_list.append((genres[i], plays[i], i))
    gen_play_list = sorted(gen_play_list, key=lambda x : x[1], reverse=True)
    for i in sorted(gen_play.items(), key=lambda x : x[1], reverse=True):
        for j in gen_play_list:
            if j[0] == i[0] and count < 2:
                answer.append(j[2])
                count += 1
        count = 0
    return answer