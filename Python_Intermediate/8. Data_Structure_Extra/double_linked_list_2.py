class Node:
    data: str

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    head: Node

    def __init__(self, head = None):
        self.head = head
        self.tail = head

    
    def is_empty(self):
        return self.head is None


    def insert_first(self, new_node):
        self.head = new_node
        self.tail = self.head


    def prepend(self, data):
        new_node = Node(data)

        if self.is_empty():
            return self.insert_first(new_node)

        old_head = self.head
        self.head.prev = new_node
        self.head = new_node
        self.head.next = old_head


    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            return self.insert_first(new_node)

        old_tail = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.tail.prev = old_tail


    def delete(self, data):
        if self.head is None:
            return False

        current_node = self.head
        while current_node is not None:
            if current_node.data == data:

                if current_node == self.head:
                    self.head = current_node.next

                    if self.head is not None:
                        self.head.prev = None
                    else:
                        self.tail = None

                elif current_node == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None

                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev

                return current_node

            current_node = current_node.next
            
        return False


    def print_forward(self):
        current_node = self.head

        if current_node is None:
            print("The list is empty")
            return

        while current_node is not self.tail:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
            
        print(current_node.data, end="")
        print()
    
    def print_backward(self):
        current_node = self.tail

        if current_node is None:
            print("The list is empty")
            return

        while current_node is not self.head:
            print(current_node.data, end=" -> ")
            current_node = current_node.prev
            
        print(current_node.data, end="")
        print()

dl = DoubleLinkedList()

print("Adding elements")
dl.append("A")
dl.append("B")
dl.append("C")
dl.print_forward()
dl.print_backward()

print("Adding elements")
dl.prepend("X")
dl.print_forward()
dl.print_backward()

print(f"Deleting element: {dl.delete("B").data}")
dl.print_forward()
dl.print_backward()

