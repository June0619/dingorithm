def solution(expression):

    temp = ''
    postfix = []
    temp_stack = []
    for char in expression:
        if char.isnumeric():
            temp += char
        else:
            postfix.append(temp)
            temp_stack.append(char)
            temp = ''
    else:
        postfix.append(temp)




    print(postfix)



    answer = 0
    return answer

#answer = 60420
case_1 = "100-200*300-500+20"

solution(case_1)