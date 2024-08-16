'''
2. Min Stack
Problem: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

LeetCode Link: Min Stack

Example:

push(-2)
push(0)
push(-3)
getMin() -> Returns -3
pop()
top() -> Returns 0
getMin() -> Returns -2

'''
class stack:
    def __init__(self):
        self.stack=[]
        self.size=0

    def is_empty(self):
        return self.size==0
    
    def push(self,element):
        if self.size <len(self.stack):
            self.stack[self.size]=element

        else:
            self.stack.append(element)
            self.size +=1
        print(f"{element} is pushed to stack")
        return element
    
    def pop(self):
        if not self.is_empty():
            self.size -=1
            item=self.stack[self.size]

            print(f"{item} is poped")
            return item
        else:
            print(" stack is empty!!")
            return None
        
    def top(self):

        print(f"the top element is {self.stack[self.size-1]}")

    def getmin(self):
        min=self.stack[0]

        if self.is_empty():
            return None
        for i in range(1,self.size):
            if self.stack[i]<min:
                min=self.stack[i]
                
        
        print(f"{min} it is minimum")
        return min
    
obj=stack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.getmin()
obj.pop()
obj.top()
obj.getmin()



