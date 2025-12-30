from bisect import bisect_left
from itertools import product


def solution(p_info_array, p_query_array):

    #언어 직군 경력 푸드 조합 생성
    all_category = [['cpp', 'java', 'python', '-'],['backend', 'frontend', '-'],['junior', 'senior', '-'],['chicken', 'pizza', '-']]

    all_scores = {}
    for p in list(product(all_category[0], all_category[1], all_category[2], all_category[3])):
        all_scores[' '.join(list(p))] = []

    # info array 분해 후 채점
    for info_string in p_info_array:
        temp = info_string.split()
        info_score = int(temp[4])
        info_data = temp[:4]

        info_category = [[item, '-'] for item in info_data]

        for p in product(*info_category):
            all_scores[' '.join(p)].append(info_score)

    # 값이 있는 모든 배열 정렬
    for key in all_scores.keys():
        if all_scores[key]:
            all_scores[key].sort()

    result = []

    for i in range(len(p_query_array)):
        q = p_query_array[i].split()

        query_condition = q[0] + ' ' + q[2] + ' ' + q[4] + ' ' + q[6]
        query_score = int(q[7])

        if query_condition in all_scores:
            score_array = all_scores[query_condition]
            if score_array:
                idx = bisect_left(score_array, query_score)
                result.append(len(score_array) - idx)
            else:
                result.append(0)
        else:
            result.append(0)

    return result

# info_array = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
# query_array = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
#
# print(solution(info_array, query_array))