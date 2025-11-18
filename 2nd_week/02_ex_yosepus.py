# BOJ 1158
from collections import deque

def josephus_problem(n, k):

    answer_arr = []
    dq = deque([i for i in range(1, n + 1)])

    while dq:
        dq.rotate(-(k-1))
        answer_arr.append(dq.popleft())

    answer = '<' + ', '.join(str(x) for x in answer_arr) + '>'
    print(answer)

n, k = map(int, input().split())
josephus_problem(n, k)