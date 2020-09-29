"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

# Singly list

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

# add_to_head performance:
    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if not self.tail:
            # set the new node as the tail if the list is currently empty
            self.tail = new_node

# add_to_tail performance:
    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head:
            # set the new node as the head if the list is currently empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

# remove_head performance:
    def remove_head(self):
        if not self.head:
            # the list is already empty
            return None

        removed_value = self.head.get_value()
        self.head = self.head.next
        if not self.head:
            # the list is now empty as the one and only item was removed
                self.tail = None
        return removed_value

# remove tail performance:
    def remove_tail(self):
        if not self.head:
            # the list is already empty
            return None

        curr = self.head
        prev = curr
        while curr.get_next() != None:
            prev = curr
            curr = curr.get_next()

        prev.set_next(None)
        self.tail = prev
        return curr

# get_max performance:
    def get_max(self):
        if not self.head:
            return None

        curr = self.head
        max_value = curr.get_value()
        while curr != None:
            max_value = max(max_value, curr.get_value())
            curr = curr.get_next()
        return max_value

# contains performance:
    def contains(self, value):
        curr = self.head
        while curr != None:
            if curr.get_value() is value:
                return True
            curr = curr.get_next()
        return False

# # 2 Queue (using a linked list)
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def isEmpty(self):
        return self.size == 0

    # len performance: O(1)
    def __len__(self):
        return self.size

    # push performance: O(1)
    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    # pop performance: O(1)
    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #check if the new node's value is less than the current node's value.
        if value < self.value:
            #if there's no left child alredy here
            if self.left is None:
                #add new node to the left
                #create a BSTNode and encapsulate the value in it then set it to the left
                self.left = BSTNode(value)
                #otherwise call insert on the left node
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the value of the current node matches the target
        if target == self.value:
            return True
        elif target < self.value:
            return self.left.contains(target) if self.left else False
        else:
            return self.right.contains(target) if self.right else False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()
    # Call the function `fn` on the value of each node
    
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if not self:
            return
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft()  
