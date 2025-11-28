class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            print("empty_stack")
            return -1
        prv_head = self.head
        self.head = prv_head.next

        return prv_head.data

    def peek(self):
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None