from collections import deque


def is_correct_string(string):
    stack = list(string)
    temp_cnt = 0
    while stack:
        if stack.pop() == ')':
            temp_cnt += 1
        else:
            temp_cnt -= 1
        if temp_cnt < 0:
            return False

    return temp_cnt == 0

def convert_u(string):
    dq = deque(list(string))
    dq.popleft()
    dq.pop()

    for i in range(len(dq)):
        if dq[i] == '(':
            dq[i] = ')'
        else:
            dq[i] = '('

    return ''.join(dq)

def get_correct_parentheses(balanced_parentheses_string):

    if not balanced_parentheses_string:
        return ''

    dq = deque(list(balanced_parentheses_string))

    char_count = 0
    u = ''
    v = ''
    while True:
        popped = dq.popleft()
        if popped == '(':
            char_count += 1
        else:
            char_count -= 1

        u += popped

        if char_count == 0:
            while dq:
                v += dq.popleft()
            break

    if is_correct_string(u):
        return u + get_correct_parentheses(v)
    else:
        empty_string = ''

        # 4-1
        empty_string += '('

        # 4-2
        empty_string += get_correct_parentheses(v)

        # 4-3
        empty_string += ')'

        # 4-4
        empty_string += convert_u(u)

        return empty_string

    #() ))((()
    # () / ))((()
    # -> ))((()
    # -> ))(( / ()
    # -> ))(( / ( () )
    # -> (())()
    # ()(())()

    return

print(get_correct_parentheses("()))((()"))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))