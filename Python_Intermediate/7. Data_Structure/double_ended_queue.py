class Node:
    data: str

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleEndedQueue():
    def __init__(self, head = None):
        self.head = head
        self.tail = head


    def push_left(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node


    def push_right(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node


    def pop_left(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        if self.head is not None:
            self.head = self.head.next
            self.head.prev = None


    def pop_right(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        if self.tail is not None:
            self.tail = self.tail.prev
            self.tail.next = None


    def print_structure(self):
        current = self.head

        while current:
            label = ""
            if current == self.head:
                label += " <- head"
            if current == self.tail:
                label += " <- tail"
            print(f"{current.data}{label}")
            current = current.next


first_node = Node("0")

double_ended = DoubleEndedQueue()

print("Adding element")

double_ended.push_left(Node("-1"))
double_ended.push_right(Node("2"))
double_ended.print_structure()

print("Adding element")

double_ended.push_left(Node("5"))
double_ended.push_right(Node("6"))
double_ended.print_structure()

print("Deleting element")

double_ended.pop_left()
double_ended.pop_right()
double_ended.print_structure()