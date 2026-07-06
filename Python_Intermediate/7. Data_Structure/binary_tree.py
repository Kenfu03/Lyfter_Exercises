class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree():
    root : Node

    def __init__(self, root = None):
        self.root = root

    
    def insert(self, node):
        if self.root is None:
            self.root = node
            return

        self._insert(self.root, node)

    def _insert(self, current, node):
        if node.data < current.data:
            if current.left is None:
                current.left = node
            else:
                self._insert(current.left, node)
        else:
            if current.right is None:
                current.right = node
            else:
                self._insert(current.right, node)


    def print_tree(self):
        self._print(self.root, 0)

    def _print(self, node, level):
        if node is None:
            return

        self._print(node.right, level + 1)
        print("    " * level + str(node.data))
        self._print(node.left, level + 1)


root = Node(4)
tree = BinaryTree(root)
tree.insert(Node(3))
tree.insert(Node(15))
tree.insert(Node(12))
tree.insert(Node(1))
tree.print_tree()