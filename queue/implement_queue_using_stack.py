'''
Implement Queue using Stacks

Problem: LeetCode 232
Difficulty: Easy
Description: Implement a queue using two stacks.
'''


class queue:
    def __init__(self):
        self.items=[]
        self.size=0

    def enqueue(self,value):
        self.items.append(value)
        self.size +=1
        print(f"{value}is added to queue")

    def is_empty(self):
        return self.size==0

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            removed_item = self.items.pop(0)
            self.size -= 1
            print(f"{removed_item} is removed from the queue")
            return removed_item


    def peek(self):
        return self.items[0]

    def display(self):
        print(self.items[:self.size])

custom_queue=queue()
custom_queue.is_empty()
custom_queue.enqueue(10)
custom_queue.enqueue(20)
custom_queue.enqueue(30)
custom_queue.enqueue(40)

custom_queue.display()
print(custom_queue.peek())
    