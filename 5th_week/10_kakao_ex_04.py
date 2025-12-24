from itertools import permutations


def solution(expression):
    permutation_list = list(permutations(['*', '-', '+'], 3))

    answer = 0
    for case in permutation_list:
        fix = to_post_fix(expression, list(case))
        answer = max(answer, calculate_postfix(fix))

    return answer

def to_post_fix(expression, operator_rank):
    rank_dict = {}
    for i in range(len(operator_rank)):
        rank_dict[operator_rank[i]] = i

    temp = ''
    postfix_stack = []
    operator_stack = []
    for char in expression:
        if char.isnumeric():
            temp += char
        else:
            # 연산자일 경우
            # 여태까지 모은 숫자들 스택에 밀기
            postfix_stack.append(temp)

            # 랭크가 더 높을 경우
            while operator_stack and rank_dict[char] <= rank_dict[operator_stack[-1]]:
                postfix_stack.append(operator_stack.pop())
            operator_stack.append(char)
            temp = ''
    else:
        postfix_stack.append(temp)
        while operator_stack:
            postfix_stack.append(operator_stack.pop())

    return postfix_stack

def calculate_postfix(postfix_array):
    stack = []
    for c in postfix_array:
        if c.isnumeric():
            stack.append(int(c))
        else:
            right_int = stack.pop()
            left_int = stack.pop()

            if c == '+':
                stack.append(left_int + right_int)
            elif c == '-':
                stack.append(left_int - right_int)
            elif c == '*':
                stack.append(left_int * right_int)

    return stack[0] if stack[0] > 0 else -stack[0]

#answer = 60420
case_1 = "100-200*300-500+20"

solution(case_1)