from collections import deque

balanced_parentheses_string = "()))((()"


def is_correct_string(string):
    stack = list(string)
    temp_cnt = 0
    while stack:
        if stack.pop() == ')':
            temp_cnt += 1
        else:
            temp_cnt -= 1

    return temp_cnt == 0


def get_correct_parentheses(balanced_parentheses_string):

    dq = deque(list(balanced_parentheses_string))

    char_count = 0
    while True:
        if dq.popleft() == '(':
            pass







    return is_correct_string(balanced_parentheses_string)

    #( ) )) (( ()
    # () / ))((()
    # -> ))((()
    # -> ))(( / ()
    # -> ))(( / ( () )
    # -> (())()
    # ()(())()

    return


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))