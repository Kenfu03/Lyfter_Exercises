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

    def bubble_sort(self):
        values = []
        self._collect_values(self.root, values)

        n = len(values)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if values[j] > values[j + 1]:
                    values[j], values[j + 1] = values[j + 1], values[j]
                    swapped = True
            if not swapped:
                break

        return values

    def _collect_values(self, node, values):
        if node is None:
            return

        values.append(node.data)
        self._collect_values(node.left, values)
        self._collect_values(node.right, values)


if __name__ == "__main__":
    tree = BinaryTree(Node(4))

    print("Adding elements")
    tree.insert(Node(23))
    tree.insert(Node(14))
    tree.insert(Node(-12))
    tree.insert(Node(123))
    tree.print_tree()

    print("Sorting structure")
    print(tree.bubble_sort())
