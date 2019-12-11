class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next


class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


node1 = Node(12)
node2 = Node(99)
node3 = Node(37)
node1.next = node2  # 12->99
node2.next = node3  # 99->37

node1.traverse()