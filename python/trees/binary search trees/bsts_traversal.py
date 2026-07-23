class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# building the tree
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# traversing the tree
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value)
        inorder_traversal(root.right)

root = None
values = [50, 30, 70, 20, 40, 60, 80]

for val in values:
    root = insert(root, val)

# Perform inorder traversal
inorder_traversal(root)

