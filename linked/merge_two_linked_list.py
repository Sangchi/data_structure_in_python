'''
Merge Two Sorted Lists (Easy)
Merge two sorted linked lists and return it as a new sorted list.

'''

class Node:

    def __init__(self, value=0, next=None):

        self.value = value
        self.next = next

class MergeTwoLinkedLists:

    def __init__(self):
        self.head = None
    
    def merge(self, l1: Node, l2: Node) -> Node:

        dummy = Node()
        tail = dummy 

        while l1 and l2:
            if l1.value <= l2.value:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        return dummy.next

    def print_list(self, head: Node):

        current = head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')


if __name__ == "__main__":

    l1 = Node(1, Node(3, Node(5)))

    l2 = Node(2, Node(4, Node(6)))

    merger = MergeTwoLinkedLists()
    merged_list_head = merger.merge(l1, l2)

    print("Merged list:")
    merger.print_list(merged_list_head)
