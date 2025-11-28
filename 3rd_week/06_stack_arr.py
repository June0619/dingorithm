class Stack:
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)
        return

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            print("empty_stack")
            return -1

        return self.array.pop(-1)

    def peek(self):
        return self.array[-1]

    # isEmpty 기능 구현
    def is_empty(self):
        return len(self.array) == 0

s = Stack()

s.push(10)
s.push(20)

print(s.pop())

print(s.peek())

print(s.pop())

print(s.is_empty())

