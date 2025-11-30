class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)

        idx = len(self.items) - 1
        parent_idx = idx // 2
        while parent_idx > 0 and self.items[idx] > self.items[parent_idx]:
            self.items[idx], self.items[parent_idx] = self.items[parent_idx], self.items[idx]
            idx = parent_idx
            parent_idx = idx // 2

        return

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!