# Python program to implement the Operations on Stack by inheriting list class.

class Stack(list):
    def is_empty(self):
        return len(self)==0
    

    def push(self,data):
        self.append(data)


    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty")
        

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")
        

    def size(self):
        return len(self)
    
    # We have to block the insert function of the list cause in stack we can't insert in the middle 
    def insert(self,index,data):
        raise AttributeError("No attribute 'insert' in Stack")
    

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(f"Top value is: {s1.peek()}")
s1.pop()
print(f"Top value is: {s1.peek()}")