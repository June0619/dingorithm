class Node:
    def __init__(self, data, prev):
        self.data = data
        self.next = None
        self.prev = prev

class LinkedList:
    def __init__(self, value):
        self.head = Node(value, None)
        self.tail = self.head

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value, cur)
        self.tail = cur.next

    def get_kth_node_from_last(self, k):
        cur = self.tail
        for _ in range(k-1):
            if cur.prev is None:
                return cur
            cur = cur.prev

        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(1).data)  # 7이 나와야 합니다!