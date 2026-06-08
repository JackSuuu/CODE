class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        # Construct a new node instance
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current_node = self.head
            # Find the place that current_node.next is None
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            # Taking new node as the head
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            # Moving the head to the next
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            elements.append('-->')
            current = current.next
        elements.append(None)
        for each in elements:
            print(each, end=' ')


my_linked_list = LinkedList()
my_linked_list.append('Jack')
my_linked_list.append('Sheldon')
my_linked_list.append('Jacky')
my_linked_list.append('David')

my_linked_list.display()

print(' ')
my_linked_list.prepend('Janet')

my_linked_list.display()