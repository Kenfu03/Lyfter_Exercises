class Node:
    data: str

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def delete(self, target_data):
        if self.head is None:
            return

        if self.head.data == target_data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == target_data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def bubble_sort(self):
        if self.head is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current_node = self.head

            while current_node is not None and current_node.next is not None:
                if current_node.data > current_node.next.data:
                    current_node.data, current_node.next.data = (
                        current_node.next.data,
                        current_node.data,
                    )
                    swapped = True
                current_node = current_node.next

    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next


if __name__ == "__main__":
    linked_list = LinkedList(Node(35))

    print("Adding elements")
    linked_list.append(Node(8))
    linked_list.append(Node(4))
    linked_list.print_structure()

    print("Deleting element")
    linked_list.delete(8)
    linked_list.print_structure()

    print("Sorting structure")
    linked_list.bubble_sort()
    linked_list.print_structure()
