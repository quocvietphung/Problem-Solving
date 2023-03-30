class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = TreeNode(val)
        if self.root is None:
            self.root = new_node
            return
        curr_node = self.root
        while True:
            if val < curr_node.val:
                if curr_node.left is None:
                    curr_node.left = new_node
                    return
                else:
                    curr_node = curr_node.left
            elif val > curr_node.val:
                if curr_node.right is None:
                    curr_node.right = new_node
                    return
                else:
                    curr_node = curr_node.right
            else:
                return

    def traverse(self, node):
        if node is not None:
            self.traverse(node.left)
            print(node.val)
            self.traverse(node.right)

# User input request
tree = Tree()
n = int(input("Enter the number of elements in the tree: "))
print("Enter the values into the tree:")
for i in range(n):
    val = int(input())
    tree.insert(val)

print("Values in the tree in ascending order:")
tree.traverse(tree.root)
