class Node:
    data: str

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue():
    def __init__(self, head = None):
        self.head = head
        self.tail = head


    def enqueue(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            return self._enqueue(Node(data))


    def _enqueue(self, new_node):
        self.tail.next = new_node
        self.tail = new_node


    def dequeue(self):
        old_head = self.head
        self.head = self.head.next
        return old_head


    def print_all(self):
        current_node = self.head

        while current_node is not self.tail:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
            
        print(current_node.data, end="")
        print()

q = Queue()

print("Adding elements")

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.print_all()

print(f"Dequeue element: {q.dequeue().data}")

q.print_all()