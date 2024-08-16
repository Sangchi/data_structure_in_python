class Node:

    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def append(self, element):

        new_node = Node(element)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def prepend(self, element):

        new_node = Node(element)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def print_list(self):

        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def remove_last(self):

        if self.is_empty():
            return "The list is empty, no element to remove!"

        if self.head.next is None:
            self.head = None
            self.size -= 1
            return

        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None
        self.size -= 1

    def remove_specific(self, element):

        if self.is_empty():
            return "Linked list is empty"

        if self.head.value == element:
            self.head = self.head.next
            self.size -= 1
            return

        current = self.head
        while current.next and current.next.value != element:
            current = current.next

        if current.next:
            current.next = current.next.next
            self.size -= 1
        else:
            return "Element not found in the list"



list = LinkedList()

list.append(10)
list.append(20)
list.append(30)
list.append(20)
list.append(40)
list.print_list()  # Output: 10 -> 20 -> 30 -> 20 -> 40 -> None


list.remove_last()
list.print_list()  # Output: 10 -> 20 -> 30 -> 20 -> None

list.prepend(5)
list.print_list()  # Output: 5 -> 10 -> 20 -> 30 -> 20 -> None

list.remove_specific(30)
list.print_list()  # Output: 5 -> 10 -> 20 -> 20 -> None
