class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# function to insert node 
def insert(node, value):
    if Node is None:
        return Node
    else:
        if value < node.value:
            node.left = insert(node.left, value)
        if value > node.value:
            node.right = insert(node.right, value)
    return node
    