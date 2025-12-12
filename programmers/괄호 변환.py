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

def solution(p):
    if not p:
        return ''

    dq = deque(list(p))

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
        return u + solution(v)
    else:
        empty_string = ''
        empty_string += '('
        empty_string += solution(v)
        empty_string += ')'
        empty_string += convert_u(u)
        return empty_string
