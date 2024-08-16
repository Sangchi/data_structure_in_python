class stack:
    def __init__(self):
        self.stack=[]
        self.size=0

    def push(self,element):
        
        if self.size <len(self.stack):
            self.stack[self.size]=element

        else:
            self.stack.append(element)
        self.size +=1
        print(f"{element} pushed to stack")

    def pop(self):
        if not self.is_empty():
            self.size -=1
            item=self.stack[self.size]

            print(f"{item} is poped")
            return item
        else:
            print(" stack is empty!!")
            return None

    def peek(self):

        if not self.is_empty():
            peek_element=self.stack[self.size-1]
            print(f"{peek_element} is peek element")

        else:
            print("stack is empty")
            return None

    def is_empty(self):
        return self.size==0
    
    
    def display(self):
        print(self.stack[:self.size])
    
    
obj=stack()
print(obj.is_empty())
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(50)
obj.display()
obj.peek()
obj.pop()
obj.display()
obj.peek()

    
        