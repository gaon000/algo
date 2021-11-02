def solution(participant, completion):
    result = ''
    from collections import defaultdict
    completion_dict = defaultdict(int)
    for i in completion:
        completion_dict[i] += 1
    for i in participant:
        completion_dict[i] -= 1
    for i in completion_dict:
        if completion_dict[i] == -1:
            result = i
    return result

# 중첩 for로 n^2나오면 효율성 오류, hash 이용