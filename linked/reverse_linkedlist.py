class node:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next

class reverse_linked_list:
    def __init__(self):
        self.head=None
        self.prev=None
    
    def append(self,value):
        if not self.head:
            self.head=node(value)

        else:
            current=self.head
            while current.next:
                current=current.next

            current.next=node(value)



    def reverse(self):

        prev=None
        current=self.head

        while current:
            next_node=current.next   #save next node
            current.next=prev        #Reverse the current node's pointer

            prev=current             #Move prev to this node
            current=next_node        #Move to the next node

        self.head=prev

    def print_list(self):
        current=self.head

        while current:
            print(current.value,end="->")

            current=current.next

        print("none")


list=reverse_linked_list()
list.append(10)
list.append(20)
list.append(30)
list.append(40)
list.print_list()
list.reverse()
list.print_list()