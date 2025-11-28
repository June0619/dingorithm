n = int(input())
arr = list(map(int, input().split()))

class Stack:

    def __init__(self, init_arr):
        self.store = []
        self.store.extend(init_arr)

    def push(self, value):
        self.store.append(value)

    def pop(self):
        if self.is_empty():
            return -1

        return self.store.pop(-1)

    def peek(self):
        if self.is_empty():
            return -1
        return self.store[-1]

    def is_empty(self):
        return len(self.store) == 0

    def height(self):
        return len(self.store)

def solution(param_arr):
    result_array = [0] * len(param_arr)

    s1 = Stack(arr)
    s2 = Stack([])

    while not s1.is_empty():
        while not s2.is_empty() and s2.peek()[1] < s1.peek():
            pair = s2.pop()
            idx = pair[0] - 1
            result_array[idx] = s1.height()

        s2.push((s1.height(), s1.pop()))

    print(' '.join(map(str, result_array)))

solution(arr)
