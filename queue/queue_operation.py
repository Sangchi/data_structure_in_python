class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        self.items.append(value)
        self.size += 1
        print(f"{value} is added to the queue")

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            removed_item = self.items.pop(0)
            self.size -= 1
            print(f"{removed_item} is removed from the queue")
            return removed_item

    def display(self):
        print(f"Queue: {self.items}")

custom_queue = Queue()
custom_queue.enqueue(10)
custom_queue.enqueue(20)
custom_queue.enqueue(30)
custom_queue.enqueue(40)
custom_queue.display()
custom_queue.dequeue()
custom_queue.display()

