def solution(info_arr, query_string_arr):

    query_array = []
    for query_string in query_string_arr:
        query_array.append(Query(query_string))

    result = [0] * len(query_array)

    for info_str in info_arr:
        info = Info(info_str)

        for i in range(len(query_array)):
            q = query_array[i]
            match = q.is_match(info)
            if match:
                result[i] += 1

    return result

class Info:
    def __init__(self, info_str):
        condition_array = info_str.split(' ')
        self.language = condition_array[0]
        self.type = condition_array[1]
        self.grade = condition_array[2]
        self.food = condition_array[3]
        self.score = condition_array[4]

    def __str__(self):
        return self.language + ' ' + self.type + ' ' + self.grade + ' ' + self.food + ' ' + self.score

class Query:
    def __init__(self, query_str):
        query_str = query_str.replace('and', '')
        query_str = query_str.replace('  ', ' ')
        condition_array = query_str.split(' ')
        self.language = condition_array[0]
        self.type = condition_array[1]
        self.grade = condition_array[2]
        self.food = condition_array[3]
        self.score = condition_array[4]

    def __str__(self):
        return self.language + ' ' + self.type + ' ' + self.grade + ' ' + self.food + ' ' + self.score

    def is_match(self, info):
        result = (self.language == '-' or info.language == self.language)
        result = result and ('-' == self.type or info.type == self.type)
        result = result and ('-' == self.grade or info.grade == self.grade)
        result = result and ('-' == self.food or info.food == self.food)
        result = result and (int(info.score) >= int(self.score))
        return result
