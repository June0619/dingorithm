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

    def delete(self):

        self.items[1], self.items[-1] = self.items[-1], self.items[1]

        deleted = self.items.pop()
        cur_idx = 1
        last_idx = len(self.items) - 1

        while cur_idx <= last_idx:
            l_child_idx = cur_idx * 2
            r_child_idx = cur_idx * 2 + 1

            max_idx = cur_idx

            if l_child_idx <= last_idx and self.items[cur_idx] < self.items[l_child_idx]:
                max_idx = l_child_idx

            if r_child_idx <= last_idx and self.items[cur_idx] < self.items[r_child_idx]:
                max_idx = r_child_idx

            if max_idx == cur_idx:
                break

            self.items[cur_idx], self.items[max_idx] = self.items[max_idx], self.items[cur_idx]
            cur_idx = max_idx

        return deleted  # 8 을 반환해야 합니다.

max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)
max_heap.insert(10)
max_heap.insert(7)

print(max_heap.items)