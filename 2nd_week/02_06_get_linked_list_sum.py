class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self, value):
    self.head = Node(value)

  def append(self, value):
    cur = self.head
    while cur.next is not None:
      cur = cur.next
    cur.next = Node(value)

def get_integer(linked_list):
  cur = linked_list.head
  tmp = 0

  while cur is not None:
    tmp = tmp * 10
    tmp += cur.data
    cur = cur.next
  else:
    return tmp

def get_linked_list_sum(linked_list_1, linked_list_2):
  return get_integer(linked_list_1) + get_integer(linked_list_2)

linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))