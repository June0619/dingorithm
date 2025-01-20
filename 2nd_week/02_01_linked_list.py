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

  def print_all(self):
    print('---- print all ----')
    cur = self.head

    while cur.next is not None:
      print(cur.data)
      cur = cur.next
    else:
      print(cur.data)

  def get_node(self, index):
    print('---- get node ----')
    cur = self.head
    for i in range(index):
      cur = cur.next
    else:
      print(cur.data)

  def add_node(self, index, value):
    new_node = Node(value)
    if index == 0:
      new_node.next = self.head
      self.head = new_node
    else:
      cur = self.head
      for i in range(index-1):
        cur = cur.next
      else:
        new_node.next = cur.next
        cur.next = new_node

  def delete_node(self, index):
    if index == 0:
      self.head = self.head.next
    else:
      cur = self.head
      for i in range(index-1):
        cur = cur.next
      else:
        next_node = cur.next
        cur.next = next_node.next

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.print_all()
linked_list.get_node(1)
linked_list.add_node(0, 10)
linked_list.print_all()

linked_list.add_node(2, 20)
linked_list.print_all()

linked_list.delete_node(0)
linked_list.delete_node(1)
linked_list.print_all()

