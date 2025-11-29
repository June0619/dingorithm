def is_correct_parenthesis(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        else:
            if stack and stack.pop() == '(':
                pass
            else:
                return False

    if stack:
        return False

    return True

print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))