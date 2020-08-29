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
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Compare target value to node.value
        # If value > node.vale:
        if value >= self.value:
            # Go right  
            # If node.right is None:
            if self.right is None:
            # Create the new node there
                new_node = BSTNode(value)
                self.right = new_node
            else:
                # Do the same thing
                # Insert value into node.right
                self.right.insert(value)
        # Else if value < node.value
        if value < self.value:
            # Go left
            # If node.left is None:
            if self.left is None:
                # Create node
                self.left = BSTNode(value)
            else:
                # Do the same thing
                # (compare , go left or right)
                # Insert value into node.left
                self.left.insert(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Compare target value to node.value
        # If target > node.value
        if target > self.value:
            # Go right
            # If node.right is None:
            if self.right is None:
                # We've traversed the tree and have not found it
                return False
            #Else:
            # Do the same thing
            # return node.right.contains(target)
            return self.right.contains(target)
        # Else if target < node.value
        if target < self.value:
            # Go left
            # If  node.left is None: (there are no more values in the tree)
            if self.left is None:
                # We've traversed the tree and have not found it
                return False
            # Else:
            # Search the left tree for the target
            return self.left.contains(target)
        # Else we have found the target value
        return True

    # Return the maximum value found in the tree
    def get_max(self):
        # check if there is only one node or a tree with only nodes to the left
        if self.right is None:
            # max value is the current node value
            return self.value
        # other wise we need to keep going right
        else:
            return self.right.get_max()
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Will have to look at both branches
        # if there is only one node and function return the value of that function
        fn(self.value)
        # if there are leaf-nodes to the currnt tree
        # check if there are leaf-nodes to the left 
        # if there are apply the for_each method with the passed in function to the tree to the left
        if self.left is not None:
            self.left.for_each(fn)
        # check if there are leaf-nodes to the right
        # if there are apply the passed in function over each value in the tree to the right
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        # check if there is a node to the left
        if self.left is not None:
            # if there is do the same thing to the left
            self.left.in_order_print(self.left)
        # print node value
        print(self.value)
        # check if there is a node to the right
        if self.right is not None:
            # if there is do the same thing to the right
            self.right.in_order_print(self.left)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # create a queue for the nodes
        queue = []
        # add the first node to the queue
        queue.append(self)
        # while the queue is not empty
        while len(queue) > 0:
            # remove the first node from the queue
            first_node = queue.pop(0)
            # print the removed node
            print(first_node.value)
            # add all children into the queue
            if first_node.left:
                queue.append(first_node.left)
            if first_node.right:
                queue.append(first_node.right)
        return queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # create a stick for nodes
        stack = []
        # add the first node to the stack
        stack.append(self)
        # while the stack is note empty
        while len(stack) > 0:
            # get the current node from the top of the stack
            last_node = stack.pop()
            # print that node
            print(last_node.value)
            # add all children to the stack
            if last_node.left:
                stack.append(last_node.left)
            if last_node.right:
                stack.append(last_node.right)
        return stack

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node=None):
        # print the value of the node
        print(self.value)
        # check if there are nodes to the left 
        if self.left:
            # print the nodes to the left
            self.left.pre_order_dft(node)
        # check if there are nodes to the right
        if self.right:
            # print the nodes to the right
            self.right.pre_order_dft(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node=None):
        print(self.value)
        if self.left:
            self.left.pre_order_dft(node)
        if self.right:
            self.right.pre_order_dft(node)
