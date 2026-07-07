from linked_list_structure import LinkedList, Node

class Queue(LinkedList):
    def enqueue(self, new_node):
        current_node = self.head
        next_node = current_node.next
        while (next_node is not None):
            current_node = next_node
            next_node = current_node.next

        current_node.next = new_node

    def bubble_sort(self):
        super().bubble_sort()

    def dequeue(self):
        self.head = self.head.next


if __name__ == "__main__":
    third_node = Node(-1)
    second_node = Node(6, third_node)
    first_node = Node(24, second_node)

    queue = Queue(first_node)

    print("Adding element")
    queue.enqueue(Node(-78))
    queue.print_structure()

    print("Deleting element")
    queue.dequeue()
    queue.print_structure()

    print("Sorting structure")
    queue.bubble_sort()
    queue.print_structure()
