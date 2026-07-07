from linked_list_structure import LinkedList, Node


class Stack(LinkedList):
    def push(self, new_node):
        old_head = self.head
        self.head = new_node
        self.head.next = old_head

    def bubble_sort(self):
        super().bubble_sort()

    def pop(self):
        if self.head is not None:
            self.head = self.head.next


if __name__ == "__main__":
    third_node = Node(-2)
    second_node = Node(7, third_node)
    first_node = Node(3, second_node)

    stack = Stack(first_node)

    print("Adding element")
    stack.push(Node(10))
    stack.print_structure()

    print("Deleting element")
    stack.pop()
    stack.print_structure()

    print("Sorting structure")
    stack.bubble_sort()
    stack.print_structure()
