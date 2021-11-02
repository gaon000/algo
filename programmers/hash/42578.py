def solution(clothes):
    from collections import defaultdict
    answer = 1
    clothes_dict = defaultdict(int)
    for i in clothes:
        clothes_dict[i[1]] += 1
    for i in clothes_dict:
        answer *= (clothes_dict[i] + 1)
    return answer-1