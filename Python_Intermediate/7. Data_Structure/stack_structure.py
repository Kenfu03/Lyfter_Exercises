from linked_list_structure import LinkedList, Node


class Stack(LinkedList):
    def push(self, new_node):
        old_head = self.head
        self.head = new_node
        self.head.next = old_head


    def pop(self):
        if self.head is not None:
            self.head = self.head.next


third_node = Node("3")
second_node = Node("2", third_node)
first_node = Node("1", second_node)

stack = Stack(first_node)

print("Adding element")

stack.print_structure()
stack.push(Node("4"))

print("Adding element")

stack.push(Node("5"))
stack.print_structure()

print("Deleting element")

stack.pop()
stack.print_structure()