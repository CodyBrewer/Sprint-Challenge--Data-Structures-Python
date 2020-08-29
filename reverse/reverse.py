class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # reference the previous node
        # traverse the list and when we get to the end, that node is the new head
        # start at the head
        current = self.head
        # while the current node is not equal to None(an empty node)
        while current is not None:
            # set the next node to the next node of the current node
            self.next_node = current.next_node
            # then set the next node of the current node to the previous node
            current.next_node = prev
            # set the previous node to the current node
            prev = current
            # move on to the next node by setting the current node to the next node
            current = self.next_node
        # set the head of the node to the previous node
        self.head = prev
