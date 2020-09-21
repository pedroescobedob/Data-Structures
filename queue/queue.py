"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node

  def set_next_node(self, new_next):
    self.next_node = new_next

class LinkedList(Node):
  def __init__(self, first_node=None):
    self.head = first_node
    self.tail = first_node

  def add_to_head(self, value, tail):
    # create a new Node
    new_node = Node(value)
    if self.head is None:
      # create a new Node
      self.head = new_node
      self.tail = new_node
    else:
      # set next_node of my new Node to the head
      new_node.set_next_node(self.head)
      # update head attribute
      self.head = new_node

  def add_to_tail(self, value):
    # create a new Node
    new_node = Node(value)
    # 1. LL is empty
      # update to head & tail attributes
    if self.tail is None:
      # update head & tail attributes
      self.tail = new_node
      self.head = new_node
    else:
      # set next_node of my new Node to the head
      new_node.set_next_node(new_node)
      # update head attribute
      self.tail = new_node

  def remove_head(self):
    if self.head is None:
        return None
    else:
      head_value = self.head.get_value()
      if self.head == self.tail:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.get_next_node()
      return head_value

  def remove_tail(self):
    if self.tail is None and self.head is None:
      return None
    else:
      tail_value = self.tail.get_value()
      if self.tail == self.head:
        self.head = None
        self.tail = None
      else:
        head_value = self.head
        if head_value.get_next_node() != self.tail:
          head_value = head_value.get_next_node()
          head_value.set_next_node(None)
          self.tail = head_value
      return tail_value

  def contains(self, value):
    head_value = self.head
    tail_value = self.tail
    if head_value is not None and tail_value is not None:
      return head_value.get_value()
    else:
      return None

  def get_max(self):
    head_value = self.head
    max_value = []
    if head_value is None:
      return None
    else:
      while head_value != self.tail:
        max_value.append(head_value.get_value())
        head_value = head_value.get_next_node()
      max_value.append(self.tail.get_value())
      return max(max_value)


class Queue(LinkedList):
    def __init__(self):
        # super().__init__()
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, item):
        # self.add_to_tail(item)
        self.size += 1
        self.storage.add_to_tail(item)

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_head()

if __name__ == "__main__":
    a = Queue()
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    a.enqueue(4)
