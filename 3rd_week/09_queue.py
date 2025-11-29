class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        n = Node(value)
        if self.head is None:
            self.head = n
            self.tail = n
            return

        n.next = self.tail
        self.tail = n

        return

    def dequeue(self):
        if self.tail == self.head is None:
            return -1

        if self.tail == self.head:
            return_node = self.tail
            self.tail = None
            self.head = None
            return return_node.data

        temp = self.tail

        while temp.next != self.head:
            temp = temp.next

        prev_head = self.head
        temp.next = None
        self.head = temp

        return prev_head.data

    def peek(self):
        return self.head.data

    def is_empty(self):
        return self.head is None

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

